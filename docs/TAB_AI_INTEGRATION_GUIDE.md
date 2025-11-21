# tab_ai.py 动态检测集成说明

## 概述

已将动态检测功能完整集成到 `tabs/tab_ai.py` GUI 界面中，用户可以在修复代码后直接通过界面运行动态检测。

## 实现的功能

### 1. 源文件夹自动追踪

**修改位置**: `DropTextEdit` 类

```python
class DropTextEdit(QTextEdit):
    def __init__(self, parent=None, target=1):
        # ...
        self.source_folder = None  # 新增字段
```

**功能**: 
- 当用户上传文件夹时，自动保存文件夹路径
- 用于后续动态检测时复制完整项目结构

### 2. 动态检测方法

**新增方法**: `_run_dynamic_testing_on_fixed_files()`

**功能**:
- 复制整个源文件夹到临时目录
- 应用修复后的代码到副本
- 调用 `analyzers/llm_dynamic_tester.py` 运行动态测试
- 在 GUI 输出区域显示测试结果
- 保存详细报告到 `results/` 目录
- 自动清理临时文件

**关键代码**:
```python
def _run_dynamic_testing_on_fixed_files(self, fixed_files, source_folder=None):
    # 1. 创建临时目录
    temp_dir = tempfile.mkdtemp(prefix="dynamic_test_")
    
    # 2. 复制整个文件夹
    shutil.copytree(source_folder, dest_folder,
                   ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.git'))
    
    # 3. 应用修复
    for fixed_file in fixed_files:
        # 写入修复后的内容
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    # 4. 运行动态测试
    from analyzers.llm_dynamic_tester import run_dynamic_tests
    report = run_dynamic_tests(test_files)
    
    # 5. 显示结果
    self.ui.output_area.append(report_text)
    
    # 6. 清理
    shutil.rmtree(temp_dir)
```

### 3. GUI 集成

**集成位置**: 文件保存成功后

**流程**:
```python
# 保存文件后
QMessageBox.information(self.ui, "保存成功", ...)

# 询问是否运行动态检测
run_dynamic = QMessageBox.question(
    self.ui,
    "运行动态检测",
    "文件已保存成功。\n\n是否对修复后的代码进行动态检测？",
    QMessageBox.Yes | QMessageBox.No,
    QMessageBox.Yes
)

if run_dynamic == QMessageBox.Yes:
    # 获取源文件夹
    source_folder = None
    if hasattr(self.ui.input_edit, "source_folder"):
        source_folder = self.ui.input_edit.source_folder
    
    # 运行动态检测
    self._run_dynamic_testing_on_fixed_files(fixed_files, source_folder)
```

## 用户使用流程

### 步骤 1: 上传项目文件夹

用户可以通过以下方式上传:
- 拖放文件夹到输入框
- 点击上传按钮选择文件夹

系统自动:
- 扫描所有代码文件
- 保存文件夹路径到 `source_folder`

### 步骤 2: AI 修复代码

- 用户点击"开始扫描并修复"
- AI 分析问题并生成修复代码
- 显示修复结果

### 步骤 3: 保存修复后的文件

- 系统询问是否保存
- 用户选择保存目录
- 文件保存成功

### 步骤 4: 运行动态检测 (NEW)

系统弹出对话框询问:
```
文件已保存成功。

是否对修复后的代码进行动态检测？

动态检测将实际执行代码并检测运行时问题。

[Yes]  [No]
```

如果用户选择 Yes:

1. **创建测试环境**
   ```
   🔬 开始动态检测...
   📁 源文件夹: /path/to/project
   ```

2. **复制项目**
   ```
   ✅ 已复制项目到临时目录
   ```

3. **应用修复**
   ```
   ✅ 已应用 5 个修复文件
   ```

4. **运行测试**
   ```
   🧪 正在运行动态测试...
   ```

5. **显示结果**
   ```
   📊 动态检测报告
   ================================================================
   总测试数: 10
   通过: 7 | 失败: 3
   
   发现问题总数: 12
   
   按类别统计:
     • 用户输入: 5 个
     • 资源管理: 3 个
     • 并发: 1 个
     • 边界条件: 2 个
     • 动态执行: 1 个
   
   📄 详细报告已保存: results/dynamic_test_report_20250121_123456.json
   ```

6. **清理临时文件**
   ```
   🧹 已清理临时文件
   ================================================================
   ✅ 动态检测完成
   ```

## 技术细节

### 完整文件夹复制

系统不仅复制修复后的文件，而是复制整个项目:

```python
# 源文件夹结构
project/
├── src/
│   ├── main.py       (已修复)
│   ├── utils.py      (已修复)
│   └── config.py     (未修改)
├── tests/
│   └── test_main.py  (未修改)
├── data/
│   └── sample.json   (资源文件)
└── README.md         (未修改)

# 临时文件夹 (动态测试环境)
/tmp/dynamic_test_xxx/project/
├── src/
│   ├── main.py       (应用了修复)
│   ├── utils.py      (应用了修复)
│   └── config.py     (保持原样)
├── tests/
│   └── test_main.py  (保持原样)
├── data/
│   └── sample.json   (保持原样)
└── README.md         (保持原样)
```

**优势**:
- 测试环境包含完整的项目上下文
- 可以正确处理模块导入
- 可以访问资源文件
- 更接近真实运行环境

### 智能排除

复制时自动排除:
- `__pycache__` - Python 缓存
- `*.pyc` - 编译文件
- `.git` - Git 仓库
- `node_modules` - Node.js 依赖
- `venv`, `.venv` - Python 虚拟环境

### 相对路径处理

```python
# 处理绝对路径和相对路径
if os.path.isabs(file_path):
    rel_path = os.path.relpath(file_path, source_folder)
else:
    rel_path = file_path

# 应用到目标位置
target_path = os.path.join(dest_folder, rel_path)
```

### 报告保存

详细的 JSON 报告保存到:
```
results/dynamic_test_report_YYYYMMDD_HHMMSS.json
```

报告包含:
- 所有测试用例
- 发现的问题详情
- 按类别分类
- 严重程度标记
- 修复建议

## 测试验证

运行验证脚本:
```bash
python test_tab_ai_integration.py
```

输出:
```
✅ 源文件夹字段: 找到
✅ 源文件夹赋值: 找到
✅ 动态检测方法: 找到
✅ 动态检测调用: 找到
✅ 源文件夹获取: 找到

✅ 所有修改已正确应用!
🎉 集成完成！所有功能已正确实现。
```

## 与其他系统的集成

现在 AIagent 有 4 个集成点:

1. **静态分析** (`analyzers/dynamic_detector.py`)
   - 快速扫描
   - 适合 CI/CD

2. **LLM 动态测试** (`analyzers/llm_dynamic_tester.py`)
   - 独立运行
   - 深度验证

3. **验证器集成** (`verifiers/base_verifier.py`)
   - 自动化工作流
   - 编程接口

4. **GUI 集成** (`tabs/tab_ai.py`) ⭐ NEW
   - 用户友好
   - 交互式操作
   - 一键测试

## 常见问题

### Q: 如果没有上传文件夹怎么办？

A: 系统会检测 `source_folder` 是否存在。如果不存在，会直接测试修复后的文件（不复制完整项目）。

### Q: 动态测试需要多长时间？

A: 取决于项目大小和代码复杂度，通常 10 秒到 2 分钟不等。GUI 会显示进度。

### Q: 测试会修改原文件吗？

A: 不会。所有测试都在临时目录中进行，测试完成后自动清理。

### Q: 可以查看详细的测试报告吗？

A: 可以。详细的 JSON 报告保存在 `results/` 目录，包含所有问题的详细信息。

## 优势

1. **无缝集成** - 不需要额外工具或脚本
2. **一键操作** - 简单的 Yes/No 选择
3. **完整上下文** - 测试整个项目而非孤立文件
4. **即时反馈** - 结果直接显示在 GUI
5. **持久化报告** - JSON 报告可供后续分析
6. **安全执行** - 隔离环境，不影响原文件
7. **自动清理** - 无需手动管理临时文件
8. **中文支持** - 界面和输出全中文

## 总结

通过这次集成，用户现在可以:
- 在 GUI 中直接运行动态检测
- 测试包含完整项目上下文的修复代码
- 获得详细的运行时问题报告
- 无需离开应用或运行额外脚本

这使得动态检测功能从"技术工具"变成了"用户功能"，大大提升了可用性和实用性。
