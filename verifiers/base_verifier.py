"""
BaseVerifier - 所有语言验证器的基类（兼容 Finding 对象 + 修复率修正 + 动态检测）
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
import sys
import os
import shutil
import tempfile

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.common import VerificationResult
from utils.language_detector import Language


class BaseVerifier(ABC):
    """验证器基类"""

    def __init__(self, language: Language):
        self.language = language

    # ===========================================================
    # 抽象接口
    # ===========================================================
    @abstractmethod
    def verify_syntax(self, file: Dict[str, Any]) -> Dict[str, Any]:
        """语法验证（编译检查）"""
        pass

    @abstractmethod
    def verify_functionality(self, file: Dict[str, Any],
                             test_cases: List[Dict] = None) -> Dict[str, Any]:
        """功能验证（运行测试）"""
        pass

    # ===========================================================
    # 主验证流程
    # ===========================================================
    def verify(self, original_file: Dict[str, Any],
               fixed_file: Dict[str, Any],
               original_issues: List[Any],
               test_cases: List[Dict] = None,
               scanner=None,
               enable_dynamic_testing: bool = True,
               source_folder: str = None) -> VerificationResult:
        """
        主验证流程
        
        Args:
            original_file: 原始文件信息
            fixed_file: 修复后文件信息
            original_issues: 原始问题列表
            test_cases: 测试用例
            scanner: 扫描器实例
            enable_dynamic_testing: 是否启用动态测试
            source_folder: 源文件夹路径（用于动态测试）
        """
        filename = fixed_file.get("file", "")
        result = VerificationResult(
            file=filename,
            language=self.language.value,
            compile_success=False,
            test_success=False,
            remaining_issues=[],
            new_issues=[],
            fix_rate=0.0
        )

        # --- Step 0: 统计原始问题 ---
        original_count = self._get_original_issue_count(original_issues, fixed_file)
        print(f"[BaseVerifier] 原始问题总数: {original_count}")

        # --- Step 1: 编译检查 ---
        try:
            syntax_result = self.verify_syntax(fixed_file)
            result.compile_success = syntax_result.get("success", False)
            if result.compile_success:
                print(f"[BaseVerifier] ✅ 编译成功")
            else:
                print(f"[BaseVerifier] ❌ 编译失败")
                result.error_message = "编译失败: " + str(syntax_result.get("errors", []))
        except Exception as e:
            result.error_message = f"语法验证异常: {e}"
            print(f"[BaseVerifier] 语法验证异常: {e}")
            import traceback; traceback.print_exc()

        # --- Step 2: 重新扫描 ---
        remaining_issues, new_issues, scan_success = [], [], False
        if scanner:
            try:
                print(f"[BaseVerifier] 开始重新扫描...")
                rescan_result = self._safe_scan(scanner, fixed_file)
                if rescan_result is not None:
                    remaining_issues, new_issues = self._compare_issues(original_issues, rescan_result)
                    scan_success = True
                    print(f"[BaseVerifier] 重新扫描完成: 剩余={len(remaining_issues)} 新增={len(new_issues)}")
                else:
                    print(f"[BaseVerifier] 重新扫描返回空结果")
            except Exception as e:
                print(f"[BaseVerifier] 重新扫描异常: {e}")
                import traceback; traceback.print_exc()
                result.error_message = f"重新扫描失败: {e}"

        # --- Step 3: 修复率计算 ---
        if scan_success:
            remaining_count = len(remaining_issues)
            fixed_count = max(0, original_count - remaining_count)
            if original_count > 0:
                result.fix_rate = (fixed_count / original_count) * 100
            else:
                result.fix_rate = 100.0 if remaining_count == 0 else 0.0
            print(f"[BaseVerifier] 修复率计算（实际）: {result.fix_rate:.1f}%")
        else:
            # 扫描失败时降级估算
            result.fix_rate = self._estimate_fix_rate(original_count, result.compile_success, fixed_file)
            print(f"[BaseVerifier] 修复率估算: {result.fix_rate:.1f}%")

        # --- Step 4: 编译失败修正（强制修复率=0） ---
        if not result.compile_success:
            result.fix_rate = 0.0

        # --- Step 5: 功能验证 ---
        if test_cases:
            try:
                test_result = self.verify_functionality(fixed_file, test_cases)
                result.test_success = test_result.get("success", False)
            except Exception as e:
                result.test_success = False
                print(f"[BaseVerifier] 功能验证异常: {e}")
        else:
            result.test_success = True

        # --- Step 6: 动态测试（新增） ---
        dynamic_test_result = None
        if enable_dynamic_testing and result.compile_success and source_folder:
            try:
                print(f"[BaseVerifier] 开始动态测试...")
                dynamic_test_result = self.run_dynamic_tests(source_folder, [fixed_file])
                
                if dynamic_test_result and dynamic_test_result.get("enabled"):
                    total_issues = dynamic_test_result.get("total_issues", 0)
                    print(f"[BaseVerifier] ✅ 动态测试完成: 发现 {total_issues} 个问题")
                    
                    # 将动态测试结果添加到验证结果中
                    if not hasattr(result, 'dynamic_test_result'):
                        result.dynamic_test_result = dynamic_test_result
                else:
                    print(f"[BaseVerifier] 动态测试未启用或失败")
            except Exception as e:
                print(f"[BaseVerifier] 动态测试异常: {e}")
                import traceback
                traceback.print_exc()

        # --- 汇总结果 ---
        result.remaining_issues = remaining_issues
        result.new_issues = new_issues
        
        # 如果有动态测试结果，添加到结果中
        if dynamic_test_result:
            result.dynamic_test_result = dynamic_test_result
        
        return result

    # ===========================================================
    # 工具函数区
    # ===========================================================
    def _get_original_issue_count(self, original_issues: List[Any],
                                  fixed_file: Dict[str, Any]) -> int:
        if original_issues:
            print(f"[BaseVerifier] 从 original_issues 获取: {len(original_issues)} 个问题")
            return len(original_issues)
        if "original_issues" in fixed_file:
            issues = fixed_file.get("original_issues", [])
            if isinstance(issues, list):
                print(f"[BaseVerifier] 从 fixed_file.original_issues 获取: {len(issues)} 个问题")
                return len(issues)
        if "fixed_count" in fixed_file:
            return fixed_file.get("fixed_count", 0)
        return 0

    def _safe_scan(self, scanner, fixed_file: Dict[str, Any]) -> Optional[List[Any]]:
        """
        安全调用 scanner 进行重新扫描
        优先级：scan_file() > scan([fixed_file])
        """
        try:
            # 方法1：优先使用 scan_file()（扫描单个文件）
            if hasattr(scanner, "scan_file"):
                print(f"[BaseVerifier] 使用 scanner.scan_file() 重新扫描")
                res = scanner.scan_file(fixed_file)
                return self._extract_issues_from_scan_result(res)

            # 方法2：使用 scan([fixed_file])（传入文件列表）
            if hasattr(scanner, "scan"):
                print(f"[BaseVerifier] 使用 scanner.scan([fixed_file]) 重新扫描")

                # 🔥 关键修复：必须先设置 scanner 的文件列表
                if hasattr(scanner, "files"):
                    scanner.files = [fixed_file]
                    print(f"[BaseVerifier]   已更新 scanner.files: {fixed_file.get('file', '?')}")

                # 调用 scan()
                res = scanner.scan()
                return self._extract_issues_from_scan_result(res)

            # 方法3：都不支持
            raise Exception("scanner 不支持 scan_file() 或 scan() 方法")

        except Exception as e:
            print(f"[BaseVerifier] Scanner 调用失败: {e}")
            import traceback
            traceback.print_exc()
            return None

    def _extract_issues_from_scan_result(self, rescan_result) -> List[Any]:
        if not rescan_result:
            return []
        if isinstance(rescan_result, dict):
            return (
                rescan_result.get("issues", [])
                or rescan_result.get("builtin", [])
                or rescan_result.get("findings", [])
                or []
            )
        if isinstance(rescan_result, list):
            return rescan_result
        return []

    def _compare_issues(self, original_issues: List[Any],
                        current_issues: List[Any]) -> tuple:
        """兼容 dict/Finding 两种类型"""
        # 转 dict 格式
        def normalize(issue):
            if isinstance(issue, dict):
                return issue
            if hasattr(issue, "__dict__"):
                return issue.__dict__
            return {}

        original_issues = [normalize(i) for i in original_issues]
        current_issues = [normalize(i) for i in current_issues]

        original_signatures = {self._get_issue_signature(i) for i in original_issues}
        remaining, new = [], []
        for issue in current_issues:
            sig = self._get_issue_signature(issue)
            (remaining if sig in original_signatures else new).append(issue)
        return remaining, new

    def _get_issue_signature(self, issue: Any) -> str:
        """生成问题签名，兼容 Finding 对象"""
        if not isinstance(issue, dict) and hasattr(issue, "__dict__"):
            issue = issue.__dict__
        rule_id = issue.get("rule_id", "")
        line = issue.get("line", "?")
        msg = str(issue.get("message", ""))[:80]
        return f"{rule_id}:{line}:{hash(msg) % 10000}"

    def _estimate_fix_rate(self, original_count: int,
                           compile_success: bool,
                           fixed_file: Dict[str, Any]) -> float:
        if original_count == 0:
            return 100.0
        if not compile_success:
            return 0.0
        if fixed_file.get("status") == "fixed":
            return 90.0
        return 70.0

    # ===========================================================
    # 动态检测相关方法
    # ===========================================================
    def _copy_folder_with_fixes(self, source_folder: str, fixed_files: List[Dict[str, Any]]) -> str:
        """
        复制整个源文件夹，并应用修复后的文件内容
        
        Args:
            source_folder: 源文件夹路径
            fixed_files: 修复后的文件列表，每个包含 {"file": "path", "content": "..."}
        
        Returns:
            临时文件夹路径
        """
        try:
            # 创建临时目录
            temp_dir = tempfile.mkdtemp(prefix="dynamic_test_")
            print(f"[BaseVerifier] 创建临时目录: {temp_dir}")
            
            # 复制整个文件夹
            if os.path.isdir(source_folder):
                # 获取文件夹名称
                folder_name = os.path.basename(source_folder.rstrip(os.sep))
                dest_folder = os.path.join(temp_dir, folder_name)
                
                # 复制整个目录树
                shutil.copytree(source_folder, dest_folder, 
                               ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.git'))
                print(f"[BaseVerifier] 已复制文件夹: {source_folder} -> {dest_folder}")
                
                # 应用修复后的文件内容
                for fixed_file in fixed_files:
                    file_path = fixed_file.get("file", "")
                    content = fixed_file.get("content", "")
                    
                    if not file_path or not content:
                        continue
                    
                    # 计算相对路径
                    if os.path.isabs(file_path):
                        # 如果是绝对路径，尝试计算相对于源文件夹的路径
                        try:
                            rel_path = os.path.relpath(file_path, source_folder)
                        except ValueError:
                            # 如果不在源文件夹内，使用文件名
                            rel_path = os.path.basename(file_path)
                    else:
                        rel_path = file_path
                    
                    # 目标文件路径
                    target_path = os.path.join(dest_folder, rel_path)
                    
                    # 创建目录（如果不存在）
                    os.makedirs(os.path.dirname(target_path), exist_ok=True)
                    
                    # 写入修复后的内容
                    with open(target_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"[BaseVerifier] 已应用修复: {rel_path}")
                
                return dest_folder
            else:
                print(f"[BaseVerifier] 警告: 源路径不是目录: {source_folder}")
                return temp_dir
                
        except Exception as e:
            print(f"[BaseVerifier] 复制文件夹失败: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def run_dynamic_tests(self, source_folder: str, fixed_files: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        运行动态测试
        
        Args:
            source_folder: 原始源文件夹路径
            fixed_files: 修复后的文件列表
        
        Returns:
            动态测试报告
        """
        temp_folder = None
        temp_root = None
        try:
            # 导入动态测试模块
            from analyzers.llm_dynamic_tester import run_dynamic_tests
            
            # 复制文件夹并应用修复
            temp_folder = self._copy_folder_with_fixes(source_folder, fixed_files)
            
            if not temp_folder:
                return {
                    "enabled": False,
                    "error": "无法创建测试环境"
                }
            
            # 记录临时根目录（用于后续清理）
            temp_root = os.path.dirname(temp_folder)
            
            # 准备测试文件列表（在临时文件夹中的文件）
            test_files = []
            for fixed_file in fixed_files:
                file_path = fixed_file.get("file", "")
                content = fixed_file.get("content", "")
                original = fixed_file.get("original_content", "")
                
                if not file_path:
                    continue
                
                # 计算临时文件夹中的完整路径
                if os.path.isabs(file_path):
                    try:
                        rel_path = os.path.relpath(file_path, source_folder)
                    except ValueError:
                        rel_path = os.path.basename(file_path)
                else:
                    rel_path = file_path
                
                temp_file_path = os.path.join(temp_folder, rel_path)
                
                test_files.append({
                    "file": temp_file_path,
                    "content": content,
                    "original": original
                })
            
            print(f"[BaseVerifier] 准备运行动态测试: {len(test_files)} 个文件")
            
            # 运行动态测试
            result = run_dynamic_tests(test_files)
            
            print(f"[BaseVerifier] 动态测试完成: {result.get('total_tests', 0)} 个测试")
            
            return result
            
        except ImportError as e:
            print(f"[BaseVerifier] 动态测试模块未安装: {e}")
            return {
                "enabled": False,
                "error": f"动态测试模块未安装: {e}"
            }
        except Exception as e:
            print(f"[BaseVerifier] 动态测试失败: {e}")
            import traceback
            traceback.print_exc()
            return {
                "enabled": False,
                "error": str(e)
            }
        finally:
            # 清理临时文件夹（清理整个临时根目录）
            if temp_root and os.path.exists(temp_root):
                try:
                    shutil.rmtree(temp_root)
                    print(f"[BaseVerifier] 已清理临时目录: {temp_root}")
                except Exception as e:
                    print(f"[BaseVerifier] 清理临时目录失败: {e}")
