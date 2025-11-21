# AIagent - AI Code Analysis Tool

AI驱动的代码分析工具，支持Python、Java和C++多种编程语言的静态分析和动态检测。

AI-powered code analysis tool supporting static analysis and dynamic detection for Python, Java, and C++.

## 主要功能 (Key Features)

### 1. 静态代码分析 (Static Code Analysis)
- Python: ruff, pylint, mypy, bandit
- Java: PMD, Checkstyle, SpotBugs
- C/C++: cppcheck

### 2. 动态检测 (Dynamic Detection)
- 用户输入与外部数据交互检测
- 资源管理与状态依赖检测
- 并发与异步操作检测
- 边界条件与异常处理检测
- 环境依赖与配置检测
- 动态代码执行检测

详细文档: [Dynamic Detection Documentation](docs/DYNAMIC_DETECTION.md)

### 3. 多语言支持 (Multi-Language Support)
- Python (.py)
- Java (.java)
- C/C++ (.c, .cpp, .cc, .cxx)

### 4. 可视化界面 (GUI)
- PyQt5 界面
- 实时扫描结果展示
- 配置管理

## 安装 (Installation)

```bash
# 克隆仓库
git clone https://github.com/snackline/AIagent.git
cd AIagent

# 安装依赖
pip install -r requirements.txt
```

## 快速开始 (Quick Start)

### 使用动态检测

```python
from analyzers.dynamic_detector import PythonDynamicDetector

# 准备文件数据
files = [
    {
        "file": "app.py",
        "content": open("app.py").read()
    }
]

# 创建检测器并运行
detector = PythonDynamicDetector(files)
result = detector.detect_all()

# 查看结果
print(f"发现 {result['summary']['total']} 个问题")
print(f"高危: {result['summary']['by_severity']['HIGH']}")
```

### 运行测试

```bash
# 测试动态检测器
python test_dynamic_detector.py
```

## 项目结构 (Project Structure)

```
AIagent/
├── analyzers/              # 代码分析器
│   ├── base_scanner.py    # 基类扫描器
│   ├── defect_scanner.py  # Python缺陷扫描器
│   ├── java_scanner.py    # Java扫描器
│   ├── cpp_scanner.py     # C++扫描器
│   └── dynamic_detector.py # 动态检测模块
├── agents/                 # AI Agent
├── fixers/                 # 代码修复器
├── verifiers/              # 验证器
├── utils/                  # 工具函数
├── tabs/                   # UI界面
├── docs/                   # 文档
│   └── DYNAMIC_DETECTION.md
└── test_dynamic_detector.py # 测试文件
```

## 文档 (Documentation)

- [动态检测模块文档](docs/DYNAMIC_DETECTION.md)

## 贡献 (Contributing)

欢迎贡献！请阅读贡献指南后提交PR。

## 许可证 (License)

MIT License

## 联系方式 (Contact)

- GitHub Issues: https://github.com/snackline/AIagent/issues
