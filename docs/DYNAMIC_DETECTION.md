# Dynamic Detection Module

## 概述 (Overview)

动态检测模块是一个用于代码运行时安全和可靠性分析的工具，支持 Python、Java 和 C++ 三种语言。该模块通过静态代码分析技术，在代码执行前识别潜在的运行时问题。

The Dynamic Detection Module is a tool for runtime security and reliability analysis that supports Python, Java, and C++. It identifies potential runtime issues before code execution using static code analysis techniques.

## 主要功能 (Key Features)

### 1. 用户输入与外部数据交互检测 (User Input & External Data Interaction)

检测未经验证的用户输入和外部数据处理，包括：
- HTTP 请求参数（GET/POST）、Headers、Cookies
- 文件上传/读取（文件名、内容解析）
- API 调用返回值
- 第三方服务返回数据
- JSON/XML 反序列化

**示例问题 (Example Issues):**
```python
# Python - 未验证的 HTTP 参数
user_input = request.args.get('query')  # ⚠️ DYN-INPUT-002

# Java - 未验证的请求参数
String param = request.getParameter("id");  // ⚠️ JAVA-DYN-001

# C++ - 不安全的输入函数
gets(buffer);  // ⚠️ CPP-DYN-001
```

### 2. 资源管理与状态依赖检测 (Resource Management & State Dependencies)

检测资源泄漏和状态管理问题，包括：
- 文件读写（打开/关闭）
- 数据库连接池
- 网络套接字（Socket）
- 内存分配
- 锁（Lock）的获取与释放

**示例问题 (Example Issues):**
```python
# Python - 文件未使用 with 语句
f = open('test.txt', 'r')  # ⚠️ DYN-RES-001
content = f.read()
# 可能忘记 f.close()

# Java - 资源未使用 try-with-resources
FileInputStream fis = new FileInputStream("test.txt");  // ⚠️ JAVA-DYN-003

# C++ - 内存未释放
char* ptr = (char*)malloc(100);  // ⚠️ CPP-DYN-002
// 可能忘记 free(ptr)
```

### 3. 并发与异步操作检测 (Concurrency & Async Operations)

检测并发编程中的潜在问题，包括：
- 多线程/多进程处理
- 异步回调、回调函数
- 事件驱动逻辑（如消息队列消费者）
- 线程安全问题

**示例问题 (Example Issues):**
```python
# Python - 线程创建
t = threading.Thread(target=some_func)  # ⚠️ DYN-CONC-001
t.start()

# Java - 线程创建
Thread t = new Thread(() -> { ... });  // ⚠️ JAVA-DYN-004
t.start();
```

### 4. 边界条件与异常处理检测 (Boundary Conditions & Exception Handling)

检测边界条件和数值计算问题，包括：
- 循环边界
- 数值计算（除零、溢出）
- 递归调用深度

**示例问题 (Example Issues):**
```python
# Python - 数组越界风险
for i in range(10):
    print(arr[i])  # ⚠️ DYN-BOUND-001

# Python - 除零风险
result = 10 / x  # ⚠️ DYN-BOUND-002

# Python - 递归函数
def factorial(n):
    return n * factorial(n-1)  # ⚠️ DYN-BOUND-004
```

### 5. 环境依赖与配置检测 (Environment Dependencies & Configuration)

检测环境和配置相关问题，包括：
- 配置文件读取
- 环境变量访问
- 时区与时间处理

**示例问题 (Example Issues):**
```python
# Python - 环境变量无默认值
api_key = os.getenv('API_KEY')  # ⚠️ DYN-ENV-001

# Python - 配置文件读取
config.read('app.ini')  # ⚠️ DYN-ENV-002

# Python - 时区问题
now = datetime.now()  # ⚠️ DYN-ENV-003
```

### 6. 动态代码执行检测 (Dynamic Code Execution)

检测危险的动态代码执行，包括：
- Python 中的 eval()/exec() 函数
- Java 和 C# 的反射
- JSON/XML 反序列化漏洞
- Pickle 序列化安全

**示例问题 (Example Issues):**
```python
# Python - eval/exec
result = eval(user_input)  # ⚠️ DYN-EXEC-001 (HIGH)
exec(code_string)  # ⚠️ DYN-EXEC-001 (HIGH)

# Python - Pickle 反序列化
obj = pickle.loads(data)  # ⚠️ DYN-EXEC-004 (HIGH)

# Python - YAML unsafe load
data = yaml.load(content)  # ⚠️ DYN-EXEC-005 (HIGH)

# Java - 反射
Class<?> clazz = Class.forName(className);  // ⚠️ JAVA-DYN-006 (HIGH)
```

## 使用方法 (Usage)

### 1. Python 代码检测

```python
from analyzers.dynamic_detector import PythonDynamicDetector

# 准备文件数据
files = [
    {
        "file": "app.py",
        "content": "... your Python code ..."
    }
]

# 创建检测器
detector = PythonDynamicDetector(files)

# 执行所有检测
result = detector.detect_all()

# 查看结果
print(f"总问题数: {result['summary']['total']}")
print(f"高危问题: {result['summary']['by_severity']['HIGH']}")

# 按类别查看问题
for category, findings in result['categories'].items():
    print(f"\n{category}: {len(findings)} 个问题")
    for finding in findings:
        print(f"  - [{finding['severity']}] {finding['message']}")
        print(f"    位置: {finding['file']}:{finding['line']}")
        print(f"    建议: {finding['suggestion']}")
```

### 2. Java 代码检测

```python
from analyzers.dynamic_detector import JavaDynamicDetector

files = [
    {
        "file": "Main.java",
        "content": "... your Java code ..."
    }
]

detector = JavaDynamicDetector(files)
result = detector.detect_all()
```

### 3. C/C++ 代码检测

```python
from analyzers.dynamic_detector import CppDynamicDetector

files = [
    {
        "file": "main.cpp",
        "content": "... your C++ code ..."
    }
]

detector = CppDynamicDetector(files)
result = detector.detect_all()
```

### 4. 集成到现有扫描器

动态检测已集成到现有的语言扫描器中：

```python
from analyzers.defect_scanner import DefectScanner
from analyzers.java_scanner import JavaScanner
from analyzers.cpp_scanner import CppScanner

# Python 扫描器
scanner = DefectScanner(files)
result = scanner.scan(enable_dynamic=True)
print(result['dynamic']['dynamic_detection'])

# Java 扫描器
scanner = JavaScanner(files)
result = scanner.scan_dynamic()
print(result['dynamic_detection'])

# C++ 扫描器
scanner = CppScanner(files)
result = scanner.check_compilation()
print(result['dynamic_detection'])
```

## 输出格式 (Output Format)

检测结果以字典形式返回，包含以下结构：

```python
{
    "enabled": True,
    "categories": {
        "user_input": [
            {
                "file": "test.py",
                "line": 10,
                "col": 4,
                "category": "user_input",
                "severity": "HIGH",
                "rule_id": "DYN-INPUT-001",
                "message": "HTTP 请求 get() 可能包含未验证的参数",
                "snippet": "data = requests.get(url)",
                "suggestion": "建议验证请求参数，使用参数化查询，并添加输入清理"
            },
            ...
        ],
        "resource_management": [...],
        "concurrency": [...],
        "boundary_conditions": [...],
        "environment_config": [...],
        "dynamic_execution": [...]
    },
    "summary": {
        "total": 25,
        "by_category": {
            "user_input": 5,
            "resource_management": 8,
            "concurrency": 3,
            "boundary_conditions": 4,
            "environment_config": 2,
            "dynamic_execution": 3
        },
        "by_severity": {
            "HIGH": 10,
            "MEDIUM": 12,
            "LOW": 3
        }
    }
}
```

## 严重程度级别 (Severity Levels)

- **HIGH**: 高危问题，可能导致安全漏洞或严重运行时错误
- **MEDIUM**: 中等问题，可能影响程序稳定性或性能
- **LOW**: 低危问题，代码质量改进建议

## 规则 ID (Rule IDs)

### Python 规则
- `DYN-INPUT-001` ~ `DYN-INPUT-005`: 用户输入相关
- `DYN-RES-001` ~ `DYN-RES-004`: 资源管理相关
- `DYN-CONC-001` ~ `DYN-CONC-004`: 并发相关
- `DYN-BOUND-001` ~ `DYN-BOUND-004`: 边界条件相关
- `DYN-ENV-001` ~ `DYN-ENV-003`: 环境配置相关
- `DYN-EXEC-001` ~ `DYN-EXEC-006`: 动态执行相关

### Java 规则
- `JAVA-DYN-001` ~ `JAVA-DYN-002`: 用户输入相关
- `JAVA-DYN-003`: 资源管理相关
- `JAVA-DYN-004` ~ `JAVA-DYN-005`: 并发相关
- `JAVA-DYN-006`: 反射相关

### C/C++ 规则
- `CPP-DYN-001`: 不安全的输入函数
- `CPP-DYN-002` ~ `CPP-DYN-003`: 资源管理相关
- `CPP-DYN-004`: 边界条件相关

## 最佳实践 (Best Practices)

### 1. 定期运行检测
在代码提交前和 CI/CD 流程中集成动态检测。

### 2. 优先修复高危问题
首先处理标记为 HIGH 严重程度的问题。

### 3. 结合静态和动态分析
动态检测应与静态分析工具（如 ruff、pylint、PMD）结合使用。

### 4. 关注修复建议
每个检测结果都包含具体的修复建议，参考这些建议进行代码改进。

### 5. 自定义检测规则
根据项目需求，可以扩展检测器类添加自定义规则。

## 扩展开发 (Extension Development)

### 添加新的检测规则

1. **Python 检测规则**:
   - 在相应的 Visitor 类中添加新的 visit 方法
   - 使用 `self._add()` 方法记录问题

```python
class UserInputVisitor(ast.NodeVisitor):
    def visit_NewPattern(self, node: ast.AST):
        # 自定义检测逻辑
        if self._is_risky(node):
            self._add(node, "DYN-INPUT-XXX", 
                     "问题描述",
                     "HIGH",
                     "修复建议")
        self.generic_visit(node)
```

2. **Java/C++ 检测规则**:
   - 在相应的检测方法中添加正则匹配逻辑

```python
def detect_user_input(self):
    for filename, content in self.file_map.items():
        lines = content.splitlines()
        for i, line in enumerate(lines, 1):
            if re.search(r'pattern', line):
                self.findings.append(DynamicFinding(...))
```

### 添加新的语言支持

1. 创建新的检测器类继承自 `DynamicDetector`
2. 实现所有 6 个检测方法
3. 在 `base_scanner.py` 中添加语言支持

## 性能考虑 (Performance Considerations)

- Python 检测使用 AST 解析，对大文件可能较慢
- Java/C++ 检测使用正则表达式，性能较好
- 建议对大型项目分批处理文件
- 可以通过多线程并行处理多个文件

## 限制和注意事项 (Limitations)

1. **静态分析局限性**: 某些动态行为只能在运行时检测
2. **误报可能性**: 静态分析可能产生误报，需人工判断
3. **语言特性**: 不同语言检测深度不同，Python 使用 AST 更精确
4. **第三方库**: 对某些第三方库的特殊用法可能无法检测

## 测试 (Testing)

运行测试套件验证功能：

```bash
python test_dynamic_detector.py
```

测试输出示例：
```
============================================================
测试 Python 动态检测器
============================================================

总共发现 11 个问题

按类别统计:
  user_input: 1
  resource_management: 2
  concurrency: 1
  boundary_conditions: 2
  environment_config: 2
  dynamic_execution: 3
```

## 贡献 (Contributing)

欢迎贡献新的检测规则和语言支持！

1. Fork 项目
2. 创建功能分支
3. 添加测试用例
4. 提交 Pull Request

## 许可证 (License)

MIT License

## 联系方式 (Contact)

如有问题或建议，请提交 Issue。
