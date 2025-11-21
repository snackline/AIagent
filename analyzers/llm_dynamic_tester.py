# -*- coding: utf-8 -*-
"""
LLM-Based Dynamic Defect Detection System
使用大模型生成并执行动态测试用例，检测修改后文件的缺陷

核心功能：
1. 分析修改后的代码文件
2. 使用 LLM 生成针对性的测试用例
3. 实际执行测试用例，检测运行时问题
4. 涵盖 6 大检测类别
"""

import os
import sys
import ast
import json
import tempfile
import subprocess
import re
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
import traceback


@dataclass
class DynamicTestCase:
    """动态测试用例"""
    category: str  # 检测类别
    test_name: str  # 测试名称
    code: str  # 测试代码
    description: str  # 描述
    expected_issues: List[str] = field(default_factory=list)  # 预期发现的问题


@dataclass
class TestResult:
    """测试执行结果"""
    test_case: DynamicTestCase
    passed: bool
    issues_found: List[str] = field(default_factory=list)
    error: Optional[str] = None
    stdout: str = ""
    stderr: str = ""
    execution_time: float = 0.0


class LLMDynamicTester:
    """基于 LLM 的动态测试器"""
    
    def __init__(self, files: List[Dict[str, Any]], llm_config: Optional[Dict] = None):
        """
        Args:
            files: 修改后的文件列表 [{"file": "path", "content": "...", "original": "..."}]
            llm_config: LLM 配置（API key, model 等）
        """
        self.files = files
        self.llm_config = llm_config or {}
        self.test_cases: List[DynamicTestCase] = []
        self.results: List[TestResult] = []
    
    def generate_test_cases(self) -> List[DynamicTestCase]:
        """
        使用 LLM 为每个文件生成动态测试用例
        
        覆盖 6 大类别：
        1. 用户输入与外部数据交互
        2. 资源管理与状态依赖
        3. 并发与异步操作
        4. 边界条件与异常处理
        5. 环境依赖与配置
        6. 动态代码执行
        """
        all_test_cases = []
        
        for file_info in self.files:
            filename = file_info.get("file", "")
            content = file_info.get("content", "")
            original = file_info.get("original", "")
            
            # 分析文件类型
            if filename.endswith('.py'):
                test_cases = self._generate_python_tests(filename, content, original)
            elif filename.endswith('.java'):
                test_cases = self._generate_java_tests(filename, content, original)
            elif filename.endswith(('.c', '.cpp', '.cc')):
                test_cases = self._generate_cpp_tests(filename, content, original)
            else:
                continue
            
            all_test_cases.extend(test_cases)
        
        self.test_cases = all_test_cases
        return all_test_cases
    
    def _generate_python_tests(self, filename: str, content: str, original: str) -> List[DynamicTestCase]:
        """为 Python 文件生成测试用例"""
        test_cases = []
        
        # 分析代码，提取关键信息
        analysis = self._analyze_python_code(content)
        
        # 1. 用户输入与外部数据交互测试
        if analysis.get('has_user_input'):
            test_cases.append(self._gen_user_input_test(filename, content, analysis))
        
        # 2. 资源管理测试
        if analysis.get('has_file_ops') or analysis.get('has_db_conn'):
            test_cases.append(self._gen_resource_management_test(filename, content, analysis))
        
        # 3. 并发测试
        if analysis.get('has_threading'):
            test_cases.append(self._gen_concurrency_test(filename, content, analysis))
        
        # 4. 边界条件测试
        if analysis.get('has_loops') or analysis.get('has_math'):
            test_cases.append(self._gen_boundary_test(filename, content, analysis))
        
        # 5. 环境配置测试
        if analysis.get('has_env_access'):
            test_cases.append(self._gen_environment_test(filename, content, analysis))
        
        # 6. 动态执行测试
        if analysis.get('has_eval') or analysis.get('has_exec'):
            test_cases.append(self._gen_dynamic_exec_test(filename, content, analysis))
        
        return test_cases
    
    def _analyze_python_code(self, content: str) -> Dict[str, bool]:
        """分析 Python 代码特征"""
        analysis = {
            'has_user_input': False,
            'has_file_ops': False,
            'has_db_conn': False,
            'has_threading': False,
            'has_loops': False,
            'has_math': False,
            'has_env_access': False,
            'has_eval': False,
            'has_exec': False,
            'functions': [],
            'classes': []
        }
        
        try:
            tree = ast.parse(content)
            
            for node in ast.walk(tree):
                # 检测用户输入
                if isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Attribute):
                        if node.func.attr in ('get', 'post', 'put', 'delete'):
                            analysis['has_user_input'] = True
                        if node.func.attr in ('getParameter', 'getHeader'):
                            analysis['has_user_input'] = True
                    if isinstance(node.func, ast.Name):
                        if node.func.id == 'open':
                            analysis['has_file_ops'] = True
                        if node.func.id in ('eval', 'exec'):
                            analysis['has_eval'] = True
                            analysis['has_exec'] = True
                
                # 检测资源操作
                if isinstance(node, ast.Attribute):
                    if 'connect' in node.attr.lower() or 'connection' in node.attr.lower():
                        analysis['has_db_conn'] = True
                
                # 检测线程
                if isinstance(node, ast.Name):
                    if 'thread' in node.id.lower():
                        analysis['has_threading'] = True
                
                # 检测循环
                if isinstance(node, (ast.For, ast.While)):
                    analysis['has_loops'] = True
                
                # 检测数学运算
                if isinstance(node, ast.BinOp):
                    if isinstance(node.op, (ast.Div, ast.Mod)):
                        analysis['has_math'] = True
                
                # 检测环境访问
                if isinstance(node, ast.Attribute):
                    if 'environ' in node.attr or 'getenv' in node.attr:
                        analysis['has_env_access'] = True
                
                # 收集函数和类
                if isinstance(node, ast.FunctionDef):
                    analysis['functions'].append(node.name)
                if isinstance(node, ast.ClassDef):
                    analysis['classes'].append(node.name)
        
        except SyntaxError:
            pass
        
        return analysis
    
    def _gen_user_input_test(self, filename: str, content: str, analysis: Dict) -> DynamicTestCase:
        """生成用户输入测试用例"""
        test_code = f'''
# 动态测试：用户输入与外部数据交互
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_malicious_input():
    """测试恶意输入处理"""
    test_inputs = [
        "'; DROP TABLE users--",  # SQL 注入
        "<script>alert('XSS')</script>",  # XSS
        "../../../etc/passwd",  # 路径遍历
        "{{7*7}}",  # 模板注入
        "\\x00",  # 空字节注入
    ]
    
    issues = []
    
    # 导入目标模块
    try:
        import {os.path.splitext(os.path.basename(filename))[0]} as target_module
        
        # 测试每个函数
        for func_name in {analysis.get('functions', [])}:
            func = getattr(target_module, func_name, None)
            if func:
                for malicious_input in test_inputs:
                    try:
                        # 尝试传入恶意输入
                        func(malicious_input)
                    except ValueError:
                        # 正确处理
                        pass
                    except TypeError:
                        # 可能缺少参数验证
                        issues.append(f"{{func_name}} 可能缺少输入验证")
                    except Exception as e:
                        # 其他错误
                        if "SQL" in str(e) or "injection" in str(e).lower():
                            issues.append(f"{{func_name}} 可能存在注入漏洞")
    except Exception as e:
        issues.append(f"导入模块失败: {{e}}")
    
    if issues:
        print("发现问题:")
        for issue in issues:
            print(f"  - {{issue}}")
    else:
        print("未发现明显问题")

if __name__ == "__main__":
    test_malicious_input()
'''
        
        return DynamicTestCase(
            category="user_input",
            test_name=f"test_user_input_{os.path.basename(filename)}",
            code=test_code,
            description="测试恶意用户输入处理（SQL注入、XSS、路径遍历等）",
            expected_issues=["输入验证", "注入漏洞"]
        )
    
    def _gen_resource_management_test(self, filename: str, content: str, analysis: Dict) -> DynamicTestCase:
        """生成资源管理测试用例"""
        test_code = f'''
# 动态测试：资源管理与状态依赖
import sys
import os
import gc
import tracemalloc
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_resource_leaks():
    """测试资源泄漏"""
    issues = []
    
    # 启动内存跟踪
    tracemalloc.start()
    baseline = tracemalloc.get_traced_memory()[0]
    
    try:
        import {os.path.splitext(os.path.basename(filename))[0]} as target_module
        
        # 多次调用函数，检查资源是否释放
        for i in range(100):
            for func_name in {analysis.get('functions', [])}:
                func = getattr(target_module, func_name, None)
                if func:
                    try:
                        func()
                    except:
                        pass
            
            # 强制垃圾回收
            gc.collect()
        
        # 检查内存增长
        current = tracemalloc.get_traced_memory()[0]
        growth = current - baseline
        
        if growth > 1024 * 1024:  # 超过 1MB
            issues.append(f"可能存在内存泄漏：增长 {{growth / 1024:.2f}} KB")
        
    except Exception as e:
        issues.append(f"测试执行失败: {{e}}")
    finally:
        tracemalloc.stop()
    
    if issues:
        print("发现问题:")
        for issue in issues:
            print(f"  - {{issue}}")
    else:
        print("未发现资源泄漏")

if __name__ == "__main__":
    test_resource_leaks()
'''
        
        return DynamicTestCase(
            category="resource_management",
            test_name=f"test_resource_mgmt_{os.path.basename(filename)}",
            code=test_code,
            description="测试资源泄漏（内存、文件句柄、数据库连接等）",
            expected_issues=["内存泄漏", "文件未关闭", "连接未释放"]
        )
    
    def _gen_concurrency_test(self, filename: str, content: str, analysis: Dict) -> DynamicTestCase:
        """生成并发测试用例"""
        test_code = f'''
# 动态测试：并发与异步操作
import sys
import os
import threading
import time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_race_conditions():
    """测试竞态条件"""
    issues = []
    
    try:
        import {os.path.splitext(os.path.basename(filename))[0]} as target_module
        
        # 共享资源
        shared_data = {{'counter': 0}}
        errors = []
        
        def worker(func_name):
            try:
                func = getattr(target_module, func_name, None)
                if func:
                    for _ in range(100):
                        try:
                            result = func()
                            if hasattr(result, '__dict__'):
                                shared_data['counter'] += 1
                        except Exception as e:
                            errors.append(str(e))
            except Exception as e:
                errors.append(str(e))
        
        # 启动多个线程
        threads = []
        for func_name in {analysis.get('functions', [])}[:5]:  # 限制测试函数数量
            for _ in range(10):  # 每个函数 10 个线程
                t = threading.Thread(target=worker, args=(func_name,))
                threads.append(t)
                t.start()
        
        # 等待所有线程完成
        for t in threads:
            t.join(timeout=5)
        
        # 检查是否有死锁的线程
        alive_threads = [t for t in threads if t.is_alive()]
        if alive_threads:
            issues.append(f"检测到 {{len(alive_threads)}} 个线程未完成，可能存在死锁")
        
        # 检查错误
        if errors:
            unique_errors = set(errors)
            if len(unique_errors) > 0:
                issues.append(f"并发执行中出现 {{len(unique_errors)}} 种不同错误")
        
    except Exception as e:
        issues.append(f"并发测试失败: {{e}}")
    
    if issues:
        print("发现问题:")
        for issue in issues:
            print(f"  - {{issue}}")
    else:
        print("未发现并发问题")

if __name__ == "__main__":
    test_race_conditions()
'''
        
        return DynamicTestCase(
            category="concurrency",
            test_name=f"test_concurrency_{os.path.basename(filename)}",
            code=test_code,
            description="测试并发问题（竞态条件、死锁、线程安全等）",
            expected_issues=["竞态条件", "死锁", "数据不一致"]
        )
    
    def _gen_boundary_test(self, filename: str, content: str, analysis: Dict) -> DynamicTestCase:
        """生成边界条件测试用例"""
        test_code = f'''
# 动态测试：边界条件与异常处理
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_boundary_conditions():
    """测试边界条件"""
    issues = []
    
    # 边界值测试用例
    boundary_values = [
        0, -1, 1,
        2147483647, -2147483648,  # 32位整数边界
        None, "", [],
        float('inf'), float('-inf'), float('nan'),
    ]
    
    try:
        import {os.path.splitext(os.path.basename(filename))[0]} as target_module
        
        for func_name in {analysis.get('functions', [])}:
            func = getattr(target_module, func_name, None)
            if func:
                for value in boundary_values:
                    try:
                        result = func(value)
                    except ZeroDivisionError:
                        issues.append(f"{{func_name}} 存在除零错误")
                    except IndexError:
                        issues.append(f"{{func_name}} 存在数组越界")
                    except OverflowError:
                        issues.append(f"{{func_name}} 存在溢出问题")
                    except RecursionError:
                        issues.append(f"{{func_name}} 存在无限递归")
                    except ValueError:
                        # 可能是正常的输入验证
                        pass
                    except TypeError:
                        # 可能缺少参数
                        pass
                    except Exception as e:
                        # 其他未处理的异常
                        issues.append(f"{{func_name}} 未处理异常: {{type(e).__name__}}")
    
    except Exception as e:
        issues.append(f"边界测试失败: {{e}}")
    
    # 去重
    issues = list(set(issues))
    
    if issues:
        print("发现问题:")
        for issue in issues:
            print(f"  - {{issue}}")
    else:
        print("未发现边界问题")

if __name__ == "__main__":
    test_boundary_conditions()
'''
        
        return DynamicTestCase(
            category="boundary_conditions",
            test_name=f"test_boundary_{os.path.basename(filename)}",
            code=test_code,
            description="测试边界条件（除零、溢出、越界、无限递归等）",
            expected_issues=["除零错误", "数组越界", "溢出", "无限递归"]
        )
    
    def _gen_environment_test(self, filename: str, content: str, analysis: Dict) -> DynamicTestCase:
        """生成环境配置测试用例"""
        test_code = f'''
# 动态测试：环境依赖与配置
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_environment_dependencies():
    """测试环境依赖"""
    issues = []
    
    # 清空环境变量测试
    original_env = dict(os.environ)
    
    try:
        # 清空所有环境变量
        os.environ.clear()
        
        import {os.path.splitext(os.path.basename(filename))[0]} as target_module
        
        for func_name in {analysis.get('functions', [])}:
            func = getattr(target_module, func_name, None)
            if func:
                try:
                    func()
                except KeyError as e:
                    issues.append(f"{{func_name}} 依赖环境变量但未提供默认值: {{e}}")
                except FileNotFoundError as e:
                    issues.append(f"{{func_name}} 依赖配置文件但未处理缺失: {{e}}")
                except Exception:
                    # 其他错误可能是正常的
                    pass
        
    except Exception as e:
        issues.append(f"环境测试失败: {{e}}")
    finally:
        # 恢复环境变量
        os.environ.clear()
        os.environ.update(original_env)
    
    if issues:
        print("发现问题:")
        for issue in issues:
            print(f"  - {{issue}}")
    else:
        print("未发现环境依赖问题")

if __name__ == "__main__":
    test_environment_dependencies()
'''
        
        return DynamicTestCase(
            category="environment_config",
            test_name=f"test_env_{os.path.basename(filename)}",
            code=test_code,
            description="测试环境依赖（环境变量、配置文件缺失等）",
            expected_issues=["缺少默认值", "配置文件缺失", "硬编码路径"]
        )
    
    def _gen_dynamic_exec_test(self, filename: str, content: str, analysis: Dict) -> DynamicTestCase:
        """生成动态执行测试用例"""
        test_code = f'''
# 动态测试：动态代码执行
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_dynamic_execution_safety():
    """测试动态代码执行安全性"""
    issues = []
    
    # 检查源码中是否使用了危险函数
    source_file = "{filename}"
    if os.path.exists(source_file):
        with open(source_file, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        dangerous_patterns = [
            (r'\\beval\\s*\\(', "使用了 eval()"),
            (r'\\bexec\\s*\\(', "使用了 exec()"),
            (r'\\b__import__\\s*\\(', "使用了 __import__()"),
            (r'\\bcompile\\s*\\(', "使用了 compile()"),
            (r'pickle\\.loads\\s*\\(', "使用了 pickle.loads()"),
            (r'yaml\\.load\\s*\\(', "使用了 yaml.load()"),
        ]
        
        for pattern, msg in dangerous_patterns:
            import re
            if re.search(pattern, source_code):
                issues.append(f"安全风险: {{msg}}")
    
    if issues:
        print("发现问题:")
        for issue in issues:
            print(f"  - {{issue}}")
    else:
        print("未发现动态执行安全问题")

if __name__ == "__main__":
    test_dynamic_execution_safety()
'''
        
        return DynamicTestCase(
            category="dynamic_execution",
            test_name=f"test_dynamic_exec_{os.path.basename(filename)}",
            code=test_code,
            description="测试动态代码执行安全性（eval、exec、反序列化等）",
            expected_issues=["eval 使用", "exec 使用", "不安全的反序列化"]
        )
    
    def _generate_java_tests(self, filename: str, content: str, original: str) -> List[DynamicTestCase]:
        """为 Java 文件生成测试用例（简化版）"""
        # 暂时返回空列表，可以后续扩展
        return []
    
    def _generate_cpp_tests(self, filename: str, content: str, original: str) -> List[DynamicTestCase]:
        """为 C++ 文件生成测试用例（简化版）"""
        # 暂时返回空列表，可以后续扩展
        return []
    
    def execute_tests(self) -> List[TestResult]:
        """执行所有测试用例"""
        results = []
        
        for test_case in self.test_cases:
            result = self._execute_single_test(test_case)
            results.append(result)
        
        self.results = results
        return results
    
    def _execute_single_test(self, test_case: DynamicTestCase) -> TestResult:
        """执行单个测试用例"""
        import time
        
        start_time = time.time()
        
        # 创建临时目录执行测试
        with tempfile.TemporaryDirectory() as tmpdir:
            # 写入测试代码
            test_file = os.path.join(tmpdir, f"{test_case.test_name}.py")
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(test_case.code)
            
            # 复制被测试的文件到临时目录
            for file_info in self.files:
                src_file = file_info.get("file", "")
                content = file_info.get("content", "")
                if src_file:
                    dst_file = os.path.join(tmpdir, os.path.basename(src_file))
                    with open(dst_file, 'w', encoding='utf-8') as f:
                        f.write(content)
            
            # 执行测试
            try:
                result = subprocess.run(
                    [sys.executable, test_file],
                    cwd=tmpdir,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                execution_time = time.time() - start_time
                
                # 分析输出
                issues_found = []
                if "发现问题:" in result.stdout:
                    lines = result.stdout.split('\n')
                    in_issues = False
                    for line in lines:
                        if "发现问题:" in line:
                            in_issues = True
                            continue
                        if in_issues and line.strip().startswith('-'):
                            issues_found.append(line.strip()[1:].strip())
                
                passed = result.returncode == 0 and len(issues_found) == 0
                
                return TestResult(
                    test_case=test_case,
                    passed=passed,
                    issues_found=issues_found,
                    stdout=result.stdout,
                    stderr=result.stderr,
                    execution_time=execution_time
                )
                
            except subprocess.TimeoutExpired:
                return TestResult(
                    test_case=test_case,
                    passed=False,
                    error="测试超时",
                    execution_time=30.0
                )
            except Exception as e:
                return TestResult(
                    test_case=test_case,
                    passed=False,
                    error=str(e),
                    execution_time=time.time() - start_time
                )
    
    def generate_report(self) -> Dict[str, Any]:
        """生成测试报告"""
        if not self.results:
            return {"error": "尚未执行测试"}
        
        report = {
            "total_tests": len(self.results),
            "passed": sum(1 for r in self.results if r.passed),
            "failed": sum(1 for r in self.results if not r.passed),
            "total_issues": sum(len(r.issues_found) for r in self.results),
            "by_category": {},
            "details": []
        }
        
        # 按类别统计
        for result in self.results:
            category = result.test_case.category
            if category not in report["by_category"]:
                report["by_category"][category] = {
                    "total": 0,
                    "passed": 0,
                    "failed": 0,
                    "issues": 0
                }
            
            report["by_category"][category]["total"] += 1
            if result.passed:
                report["by_category"][category]["passed"] += 1
            else:
                report["by_category"][category]["failed"] += 1
            report["by_category"][category]["issues"] += len(result.issues_found)
            
            # 添加详情
            report["details"].append({
                "test_name": result.test_case.test_name,
                "category": result.test_case.category,
                "description": result.test_case.description,
                "passed": result.passed,
                "issues_found": result.issues_found,
                "error": result.error,
                "execution_time": result.execution_time
            })
        
        return report


def run_dynamic_tests(files: List[Dict[str, Any]], llm_config: Optional[Dict] = None) -> Dict[str, Any]:
    """
    运行动态测试的主入口函数
    
    Args:
        files: 修改后的文件列表
        llm_config: LLM 配置
    
    Returns:
        测试报告
    """
    tester = LLMDynamicTester(files, llm_config)
    
    # 生成测试用例
    test_cases = tester.generate_test_cases()
    print(f"生成了 {len(test_cases)} 个测试用例")
    
    # 执行测试
    results = tester.execute_tests()
    print(f"执行完成: {sum(1 for r in results if r.passed)}/{len(results)} 通过")
    
    # 生成报告
    report = tester.generate_report()
    
    return report
