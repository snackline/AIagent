# LLM 动态测试系统文档

## 概述

LLM 动态测试系统是一个基于大语言模型的代码缺陷检测工具，它通过**实际执行测试用例**来检测修改后文件中的运行时问题。

**关键区别**：
- **静态检测** (`dynamic_detector.py`): 分析代码结构，不执行
- **动态测试** (`llm_dynamic_tester.py`): **实际运行代码**，检测真实问题

## 核心特性

### 1. 真正的动态测试

系统会：
1. 分析修改后的代码文件
2. 自动生成针对性的测试用例
3. **实际执行测试代码**
4. 捕获运行时错误和问题

### 2. 六大检测类别

#### 类别 1: 用户输入与外部数据交互
- **检测内容**: SQL 注入、XSS、路径遍历、注入漏洞
- **测试方法**: 传入恶意输入，观察程序反应
- **示例**:
```python
# 被测试代码
def process_user_data(user_input):
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    return query

# 自动生成的测试
test_inputs = [
    "'; DROP TABLE users--",  # SQL 注入
    "<script>alert('XSS')</script>",  # XSS
    "../../../etc/passwd",  # 路径遍历
]
# 实际执行并检测是否正确处理
```

#### 类别 2: 资源管理与状态依赖
- **检测内容**: 内存泄漏、文件未关闭、连接未释放
- **测试方法**: 多次调用函数，监控资源使用
- **示例**:
```python
# 被测试代码
def read_file(filename):
    f = open(filename, 'r')  # 未关闭！
    return f.read()

# 自动生成的测试
# 启用内存跟踪
tracemalloc.start()
for i in range(100):
    read_file('test.txt')  # 重复调用
gc.collect()
# 检查内存是否增长 → 发现泄漏
```

#### 类别 3: 并发与异步操作
- **检测内容**: 竞态条件、死锁、线程安全问题
- **测试方法**: 多线程并发执行，检测数据不一致
- **示例**:
```python
# 被测试代码
counter = 0
def increment():
    global counter
    counter += 1  # 非原子操作！

# 自动生成的测试
threads = [Thread(target=increment) for _ in range(100)]
for t in threads: t.start()
for t in threads: t.join()
# 检查 counter 是否等于 100 → 发现竞态条件
```

#### 类别 4: 边界条件与异常处理
- **检测内容**: 除零、数组越界、溢出、无限递归
- **测试方法**: 传入边界值，捕获异常
- **示例**:
```python
# 被测试代码
def divide(a, b):
    return a / b  # 未检查 b == 0

# 自动生成的测试
boundary_values = [0, -1, 2147483647, None, float('inf')]
for value in boundary_values:
    try:
        divide(10, value)
    except ZeroDivisionError:
        # 发现：除零错误未处理
```

#### 类别 5: 环境依赖与配置
- **检测内容**: 环境变量缺失、配置文件不存在、硬编码
- **测试方法**: 清空环境，执行代码
- **示例**:
```python
# 被测试代码
def get_api_key():
    return os.environ['API_KEY']  # 未提供默认值

# 自动生成的测试
os.environ.clear()  # 清空环境变量
try:
    get_api_key()
except KeyError:
    # 发现：依赖环境变量但缺少默认值
```

#### 类别 6: 动态代码执行
- **检测内容**: eval/exec 使用、不安全的反序列化
- **测试方法**: 静态扫描源码
- **示例**:
```python
# 被测试代码
def execute_code(code):
    return eval(code)  # 危险！

# 自动生成的测试
# 检查源码中是否有 eval/exec/pickle.loads
# 发现：使用了 eval()
```

## 使用方法

### 快速开始

```python
from analyzers.llm_dynamic_tester import run_dynamic_tests

# 准备修改后的文件
files = [
    {
        "file": "app.py",
        "content": "... 修改后的代码 ...",
        "original": "... 原始代码 ..."  # 可选
    }
]

# 运行动态测试
report = run_dynamic_tests(files)

# 查看结果
print(f"总测试: {report['total_tests']}")
print(f"通过: {report['passed']}")
print(f"发现问题: {report['total_issues']}")
```

### 详细示例

```python
from analyzers.llm_dynamic_tester import LLMDynamicTester

# 创建测试器
tester = LLMDynamicTester(files)

# 1. 生成测试用例
test_cases = tester.generate_test_cases()
print(f"生成了 {len(test_cases)} 个测试用例")

# 2. 执行测试
results = tester.execute_tests()

# 3. 生成报告
report = tester.generate_report()

# 4. 查看详细结果
for detail in report['details']:
    if detail['issues_found']:
        print(f"\n测试: {detail['test_name']}")
        print(f"类别: {detail['category']}")
        print(f"描述: {detail['description']}")
        print("发现的问题:")
        for issue in detail['issues_found']:
            print(f"  - {issue}")
```

## 测试报告格式

```python
{
    "total_tests": 6,
    "passed": 3,
    "failed": 3,
    "total_issues": 6,
    "by_category": {
        "user_input": {
            "total": 1,
            "passed": 1,
            "failed": 0,
            "issues": 0
        },
        "resource_management": {
            "total": 1,
            "passed": 0,
            "failed": 1,
            "issues": 1
        },
        ...
    },
    "details": [
        {
            "test_name": "test_user_input_app.py",
            "category": "user_input",
            "description": "测试恶意用户输入处理",
            "passed": false,
            "issues_found": ["SQL 注入风险"],
            "error": null,
            "execution_time": 0.5
        },
        ...
    ]
}
```

## 与静态检测的对比

| 特性 | 静态检测 (dynamic_detector.py) | 动态测试 (llm_dynamic_tester.py) |
|------|-------------------------------|----------------------------------|
| **分析方式** | AST/正则分析代码结构 | 实际执行测试代码 |
| **是否运行代码** | ❌ 否 | ✅ 是 |
| **检测深度** | 表层模式匹配 | 深层运行时行为 |
| **误报率** | 较高 | 较低 |
| **执行速度** | 快（秒级） | 慢（分钟级） |
| **资源消耗** | 低 | 高 |
| **适用场景** | 快速扫描大量代码 | 深度测试关键代码 |

**建议**：两者结合使用
1. 先用静态检测快速发现明显问题
2. 再用动态测试深入验证关键代码

## 集成到项目

### 方法 1: 独立使用

```bash
# 运行演示
python demo_llm_dynamic_testing.py

# 查看各类别检测效果
```

### 方法 2: 集成到扫描器

```python
# 在 defect_scanner.py 中集成
from analyzers.llm_dynamic_tester import run_dynamic_tests

def scan_with_dynamic_tests(self):
    # 准备文件
    files = [{"file": f["file"], "content": f["content"]} 
             for f in self.files]
    
    # 运行动态测试
    report = run_dynamic_tests(files)
    
    return report
```

### 方法 3: Git Hook 集成

```bash
# .git/hooks/pre-commit
#!/bin/bash

# 获取修改的 Python 文件
MODIFIED_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')

if [ -n "$MODIFIED_FILES" ]; then
    echo "运行动态测试..."
    python run_dynamic_tests.py $MODIFIED_FILES
    
    if [ $? -ne 0 ]; then
        echo "动态测试发现问题，提交被阻止"
        exit 1
    fi
fi
```

## 性能优化

### 1. 并行执行

```python
from concurrent.futures import ThreadPoolExecutor

def execute_tests_parallel(self):
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(self._execute_single_test, tc) 
                   for tc in self.test_cases]
        results = [f.result() for f in futures]
    return results
```

### 2. 缓存测试结果

```python
import hashlib
import pickle

def cache_result(filename, content, result):
    cache_key = hashlib.md5(content.encode()).hexdigest()
    with open(f'.cache/{cache_key}.pkl', 'wb') as f:
        pickle.dump(result, f)
```

### 3. 增量测试

```python
def should_test(file_info):
    """只测试修改的部分"""
    if 'original' in file_info:
        return file_info['content'] != file_info['original']
    return True
```

## 故障排查

### 问题 1: 测试超时

**原因**: 代码有死循环或死锁

**解决**:
```python
# 降低超时时间
result = subprocess.run(..., timeout=10)  # 默认 30 秒
```

### 问题 2: 导入错误

**原因**: 缺少依赖或路径不对

**解决**:
```python
# 在测试代码中添加
sys.path.insert(0, '/path/to/project')
```

### 问题 3: 权限错误

**原因**: 测试代码尝试访问受保护的资源

**解决**:
```python
# 使用沙箱执行
import subprocess
result = subprocess.run(['python', '-m', 'sandbox', test_file])
```

## 扩展开发

### 添加新的检测类别

```python
def _gen_custom_test(self, filename, content, analysis):
    """自定义测试"""
    test_code = '''
# 你的测试代码
...
'''
    return DynamicTestCase(
        category="custom",
        test_name="test_custom",
        code=test_code,
        description="自定义检测",
        expected_issues=[]
    )
```

### 添加 LLM 生成测试用例

```python
def _gen_with_llm(self, filename, content):
    """使用 LLM 生成测试用例"""
    import openai
    
    prompt = f"""
    为以下代码生成安全测试用例：
    
    ```python
    {content}
    ```
    
    生成 pytest 测试代码，检测：
    1. 用户输入验证
    2. 资源泄漏
    3. 并发安全
    ...
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content
```

## 最佳实践

1. **测试前备份**: 动态测试会执行代码，建议在隔离环境运行
2. **限制范围**: 只对修改的文件运行动态测试
3. **结合静态**: 先静态检测，发现问题后再动态验证
4. **定期运行**: 在 CI/CD 流程中定期执行
5. **审查结果**: 人工审查测试结果，避免误判

## 总结

LLM 动态测试系统通过**实际执行代码**来检测运行时问题，是静态分析的重要补充。它特别适合：

- ✅ 检测复杂的运行时问题
- ✅ 验证安全防护是否有效
- ✅ 发现资源泄漏和性能问题
- ✅ 测试并发和异步代码
- ✅ 验证边界条件处理

与静态检测结合使用，可以提供全面的代码质量保障。
