# agents/fixer_agent.py
"""
FixerAgent - 多语言代码修复Agent
"""
import sys
import os
from typing import Dict, Any, List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .base_agent import BaseAgent
from utils.language_detector import Language, LanguageDetector
from fixers.fixer_factory import FixerFactory


class FixerAgent(BaseAgent):
    """多语言代码修复Agent"""

    def __init__(self, config: Dict[str, Any] = None):
        super().__init__("FixerAgent", config or {})
        self.llm_client = config.get("llm_client") if config else None
        self.fixers = {}

    def perceive(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """感知阶段：接收分析结果"""
        analysis = input_data.get("analysis", {})
        files = input_data.get("files", [])
        user_request = input_data.get("user_request", "")

        by_language = analysis.get("by_language", {})

        self.log(f"📊 收到分析结果：涉及 {len(by_language)} 种语言")
        for lang, lang_analysis in by_language.items():
            # ✅ 安全地获取 total
            total = lang_analysis.get("total", 0) if isinstance(lang_analysis, dict) else 0
            self.log(f"   - {lang.upper()}: {total} 个问题待修复")

        # ✅ 检查 LLM 配置
        use_llm = self.config.get("use_llm", True) and self.llm_client is not None

        # 🔥 调试：输出 LLM 配置
        print(f"\n🔥🔥🔥 [DEBUG] config.use_llm: {self.config.get('use_llm', True)}")
        print(f"🔥🔥🔥 [DEBUG] llm_client 是否存在: {self.llm_client is not None}")
        print(f"🔥🔥🔥 [DEBUG] 最终 use_llm: {use_llm}")
        print(f"🔥🔥🔥 [DEBUG] fixer config: {self.config}")
        if self.llm_client:
            print(f"🔥🔥🔥 [DEBUG] llm_client 类型: {type(self.llm_client)}")
        else:
            print(f"🔥🔥🔥 [DEBUG] llm_client 为 None!")

        return {
            "analysis": analysis,
            "files": files,
            "by_language": by_language,
            "user_request": user_request,
            "use_rules": self.config.get("use_rules", True),
            "use_llm": use_llm
        }

    def decide(self, perception: Dict[str, Any]) -> Dict[str, Any]:
        """
        决策阶段：确定修复策略

        两类策略：
        1) 正常模式：根据 Analyzer 提供的 by_language / issues_by_file 构造修复计划；
        2) 兜底模式：
           - DebugBench 专用：user_request 中包含 [DEBUGBENCH] 时，即使没有 issue，也为文件构造虚拟 issue；
           - 实际场景兜底：配置 force_llm_on_empty={lang: True} 时，对该语言在无 issue 时也尝试 LLM 修复。
        """
        by_language = perception.get("by_language", {}) or {}
        use_rules = perception.get("use_rules", True)
        use_llm = perception.get("use_llm", False)
        files = perception.get("files", []) or []
        user_request = perception.get("user_request", "") or ""

        # DebugBench 模式：通过 user_request 标记
        debugbench_mode = "[DEBUGBENCH" in user_request  # 移除结尾的 ]，匹配所有 [DEBUGBENCH 开头的标记

        # 兜底配置：可以是 bool 或 dict，例如 {"java": True}
        force_llm_cfg = self.config.get("force_llm_on_empty", False)

        def _force_llm_for_lang(lang_name: str) -> bool:
            """根据配置判断某语言是否在无 issue 时也兜底修复"""
            if isinstance(force_llm_cfg, bool):
                return force_llm_cfg
            if isinstance(force_llm_cfg, dict):
                return bool(force_llm_cfg.get(lang_name, False))
            return False

        strategy = {
            "repair_plans": [],
            "use_rules": use_rules,
            "use_llm": use_llm,
            # 在 execute 阶段还会用到 files/user_request
            "files": files,
            "user_request": user_request,
        }

        # ============================================================
        # 1️⃣ 正常路径：根据 Analyzer 提供的 by_language / issues_by_file 构造修复计划
        # ============================================================
        for lang_name, lang_analysis in by_language.items():
            if not isinstance(lang_analysis, dict):
                continue

            issues_by_file = lang_analysis.get("issues_by_file", {}) or {}
            total_issues = lang_analysis.get("total", 0) or 0

            # 如果 AnalyzerAgent 没生成 issues_by_file，就尝试从 builtin/external 提取
            if not issues_by_file:
                if "builtin" in lang_analysis or "external" in lang_analysis:
                    merged: List[Any] = []
                    for k in ["builtin", "external"]:
                        if isinstance(lang_analysis.get(k), list):
                            merged.extend(lang_analysis[k])

                    # 自动聚合成 issues_by_file 结构
                    tmp_map: Dict[str, List[Any]] = {}
                    for issue in merged:
                        filename = "unknown"
                        if isinstance(issue, dict):
                            filename = issue.get("file") or issue.get("filename") or "unknown"
                        elif hasattr(issue, "file") or hasattr(issue, "filename"):
                            filename = getattr(issue, "file", None) or getattr(issue, "filename", "unknown")
                        tmp_map.setdefault(filename, []).append(issue)

                    issues_by_file = tmp_map

                print(f"[DEBUG] 自动生成 issues_by_file: {len(issues_by_file)} 个文件 (lang={lang_name})")

            # 如果仍然没有 issue，先不为该语言创建 plan，稍后看兜底逻辑是否启用
            if not issues_by_file:
                continue

            repair_plan = {
                "language": lang_name,
                "files_to_fix": [],
                "total_issues": total_issues
            }

            for filename, issues in issues_by_file.items():
                if not isinstance(issues, list):
                    issues = [issues]

                repair_plan["files_to_fix"].append({
                    "filename": filename,
                    "issues": issues,
                    "issue_count": len(issues)
                })

            strategy["repair_plans"].append(repair_plan)

        # ============================================================
        # 2️⃣ DebugBench 兜底逻辑：
        #    如果处于 DebugBench 模式且当前没有任何修复计划，
        #    则为所有文件生成“虚拟 issue”，强制走 LLM 修复。
        # ============================================================
        if debugbench_mode and not strategy["repair_plans"]:
            print("\n[FixerAgent] ⚙️ DebugBench 模式下未发现任何问题，启用兜底修复策略：")
            print(f"[FixerAgent]    - files 数量: {len(files)}")

            # 按文件扩展名推断语言
            files_by_lang: Dict[str, List[Dict[str, Any]]] = {}
            for f in files:
                path = f.get("file", "") or ""
                lower = path.lower()
                if lower.endswith(".py"):
                    lang = "python"
                elif lower.endswith(".java"):
                    lang = "java"
                elif lower.endswith((".cpp", ".cc", ".cxx", ".c")):
                    lang = "cpp"
                else:
                    continue

                files_by_lang.setdefault(lang, []).append(f)

            for lang_name, lang_files in files_by_lang.items():
                if not lang_files:
                    continue

                print(
                    f"[FixerAgent]    - 为语言 {lang_name.upper()} 创建 DebugBench 虚拟修复计划，文件数: {len(lang_files)}")

                files_to_fix = []
                for f in lang_files:
                    fname = f.get("file", "unknown")
                    synthetic_issue = {
                        "rule_id": "DEBUGBENCH",
                        "message": "Synthetic issue for DebugBench evaluation (force LLM fix).",
                        "severity": "MEDIUM",
                        "file": fname,
                        "line": 0,
                    }
                    files_to_fix.append({
                        "filename": fname,
                        "issues": [synthetic_issue],
                        "issue_count": 1
                    })

                strategy["repair_plans"].append({
                    "language": lang_name,
                    "files_to_fix": files_to_fix,
                    "total_issues": len(files_to_fix),
                })

        # ============================================================
        # 3️⃣ 实际场景兜底逻辑：
        #    对配置 force_llm_on_empty 的语言，即使 Analyzer 认为 total=0，
        #    也为这些语言的文件创建“无 issue”计划，只供 LLM 通读修复。
        # ============================================================
        # 先找出哪些语言已经有 plan
        planned_langs = {p["language"] for p in strategy["repair_plans"]}

        # 构造按语言分组的文件
        files_by_lang_for_fallback: Dict[str, List[Dict[str, Any]]] = {}
        for f in files:
            path = f.get("file", "") or ""
            lower = path.lower()
            if lower.endswith(".py"):
                lang = "python"
            elif lower.endswith(".java"):
                lang = "java"
            elif lower.endswith((".cpp", ".cc", ".cxx", ".c")):
                lang = "cpp"
            else:
                continue
            files_by_lang_for_fallback.setdefault(lang, []).append(f)

        for lang_name, lang_files in files_by_lang_for_fallback.items():
            if not lang_files:
                continue

            # 已有正常 plan 的语言不再兜底
            if lang_name in planned_langs:
                continue

            # 未开启兜底的语言跳过
            if not _force_llm_for_lang(lang_name):
                continue

            print(
                f"\n[FixerAgent] ⚙️ 兜底模式：为语言 {lang_name.upper()} 在无 issue 情况下仍创建修复计划，文件数: {len(lang_files)}")

            files_to_fix = []
            for f in lang_files:
                fname = f.get("file", "unknown")
                # 这里不给任何“真实 issue”，只是一个空列表，让 Fixer/LLM 自行通读
                files_to_fix.append({
                    "filename": fname,
                    "issues": [],  # 🔥 对应 JavaFixer 里 issue 可能为空的情况
                    "issue_count": 0
                })

            strategy["repair_plans"].append({
                "language": lang_name,
                "files_to_fix": files_to_fix,
                "total_issues": 0,
            })

        # ============================================================
        # 4️⃣ 日志输出
        # ============================================================
        self.log(f"\n决策：制定了 {len(strategy['repair_plans'])} 个修复计划")
        self.log(f"   - 使用规则修复: {'是' if use_rules else '否'}")
        self.log(f"   - 使用LLM修复: {'是' if use_llm else '否'}")

        if debugbench_mode:
            self.log("   - DebugBench 模式：即使扫描器未发现问题，也会对文件进行修复尝试")
        if force_llm_cfg:
            self.log(f"   - 兜底模式已启用: force_llm_on_empty={force_llm_cfg}")

        return strategy

    def execute(self, decision: Dict[str, Any]) -> Dict[str, Any]:
        """执行阶段：对每种语言执行修复"""
        repair_plans = decision.get("repair_plans", [])
        use_rules = decision.get("use_rules", True)
        use_llm = decision.get("use_llm", False)
        user_request = decision.get("user_request", "")

        all_results = {
            "by_language": {},
            "fixed_files": [],
            "summary": {
                "total_files": 0,
                "successfully_fixed": 0,
                "failed": 0,
                "total_fixes": 0
            }
        }

        # 获取原始文件映射
        files = decision.get("files", [])
        file_map = {f.get("file"): f for f in files}

        print(f"\n🔥🔥🔥 [DEBUG] file_map 构建完成，共 {len(file_map)} 个文件")
        for k in list(file_map.keys())[:3]:
            print(f"🔥🔥🔥 [DEBUG] file_map key 示例: {k}")

        # 对每种语言执行修复
        for plan in repair_plans:
            lang_name = plan["language"]
            files_to_fix = plan["files_to_fix"]

            self.log(f"\n{'=' * 60}")
            self.log(f"🔧 开始修复 {lang_name.upper()} 代码...")
            self.log(f"   待修复文件数: {len(files_to_fix)}")

            try:
                # 获取语言枚举
                lang = Language.from_string(lang_name)

                # 创建修复器
                fixer = FixerFactory.create_fixer(lang, self.llm_client)

                lang_results = {
                    "language": lang_name,
                    "files": [],
                    "summary": {
                        "total": len(files_to_fix),
                        "success": 0,
                        "failed": 0
                    }
                }

                # 修复每个文件
                for file_info in files_to_fix:
                    filename = file_info["filename"]
                    issues = file_info["issues"]

                    self.log(f"\n   📄 修复文件: {filename}")
                    self.log(f"      问题数: {len(issues)}")

                    print(f"\n🔥🔥🔥 [DEBUG] 准备修复文件: {filename}")
                    print(f"🔥🔥🔥 [DEBUG] issues 数量: {len(issues)}")

                    # =========================================================
                    # 🔥 关键修复：超级增强的文件查找逻辑
                    # =========================================================
                    original_file = None
                    matched_key = None

                    # 策略 1: 精确匹配
                    if filename in file_map:
                        original_file = file_map[filename]
                        matched_key = filename
                        print(f"🔥🔥🔥 [DEBUG] ✅ 策略1成功：精确匹配 {filename}")

                    # 策略 2: 通过 basename 匹配
                    if not original_file:
                        basename_to_find = os.path.basename(filename)
                        print(f"🔥🔥🔥 [DEBUG] 策略2：尝试 basename 匹配 {basename_to_find}")

                        for full_path, file_obj in file_map.items():
                            if os.path.basename(full_path) == basename_to_find:
                                original_file = file_obj
                                matched_key = full_path
                                print(f"🔥🔥🔥 [DEBUG] ✅ 策略2成功：basename 匹配到 {full_path}")
                                break

                    # 策略 3: 路径包含关系匹配（双向，且标准化路径）
                    if not original_file:
                        print(f"🔥🔥🔥 [DEBUG] 策略3：尝试路径包含关系匹配")
                        norm_filename = filename.replace("\\", "/").lower()

                        for full_path, file_obj in file_map.items():
                            norm_full_path = full_path.replace("\\", "/").lower()

                            # 双向检查包含关系
                            if norm_filename in norm_full_path or norm_full_path in norm_filename:
                                original_file = file_obj
                                matched_key = full_path
                                print(f"🔥🔥🔥 [DEBUG] ✅ 策略3成功：路径包含匹配到 {full_path}")
                                break

                    # 策略 4: 最后兜底 - 如果只有一个文件且语言匹配，直接使用
                    if not original_file and len(file_map) == 1:
                        print(f"🔥🔥🔥 [DEBUG] 策略4：file_map 只有一个文件，直接使用")
                        matched_key = list(file_map.keys())[0]
                        original_file = file_map[matched_key]
                        print(f"🔥🔥🔥 [DEBUG] ✅ 策略4成功：使用唯一文件 {matched_key}")

                    if not original_file:
                        print(f"🔥🔥🔥 [DEBUG] ❌ 所有策略失败！无法找到文件")
                        self.log(f"      ⚠️ [严重] 未找到原始文件，跳过修复。")
                        self.log(f"         尝试查找的文件名: {filename}")
                        self.log(f"         file_map 中的可用键:")
                        for k in file_map.keys():
                            self.log(f"           - {k}")

                        lang_results["summary"]["failed"] += 1
                        all_results["summary"]["failed"] += 1

                        # ✅ 即使找不到文件，也添加一个错误记录
                        all_results["fixed_files"].append({
                            "file": filename,
                            "content": "",
                            "language": lang_name,
                            "original_content": "",
                            "fixed_count": 0,
                            "method": "none",
                            "status": "error",
                            "success": False,
                            "error_message": "未在 file_map 中找到对应的原始文件"
                        })
                        continue

                    # ✅ 找到文件后，使用 matched_key 作为最终的 filename
                    filename = matched_key
                    print(f"🔥🔥🔥 [DEBUG] 最终使用的 filename: {filename}")

                    try:
                        print(f"🔥🔥🔥 [DEBUG] 调用 fixer.fix() 开始")

                        # 执行修复
                        fix_result = fixer.fix(
                            original_file,
                            issues,
                            use_rules=use_rules,
                            use_llm=use_llm,
                            user_request=user_request
                        )

                        print(
                            f"🔥🔥🔥 [DEBUG] fixer.fix() 返回: success={fix_result.success}, method={fix_result.method}, fixed_count={fix_result.fixed_count}")

                        # 构建输出文件
                        fixed_file = {
                            "file": filename,
                            "content": fix_result.fixed_content if fix_result.success else original_file.get("content"),
                            "language": lang_name,
                            "original_content": original_file.get("content"),
                            "fixed_count": fix_result.fixed_count,
                            "method": fix_result.method,
                            "status": "fixed" if fix_result.success else "failed",
                            "success": fix_result.success,
                            "error_message": fix_result.error_message if not fix_result.success else "",
                            "original_issues": issues,
                            "original_issues_count": len(issues)
                        }

                        print(f"🔥🔥🔥 [DEBUG] 构建 fixed_file 完成，准备添加到 all_results['fixed_files']")

                        all_results["fixed_files"].append(fixed_file)
                        lang_results["files"].append(fix_result.to_dict())

                        print(f"🔥🔥🔥 [DEBUG] fixed_file 已添加，当前 fixed_files 数量: {len(all_results['fixed_files'])}")

                        # 更新统计和日志
                        if fix_result.success:
                            self.log(f"      ✅ 修复成功！ (方法: {fix_result.method}, 修复数: {fix_result.fixed_count})")
                            lang_results["summary"]["success"] += 1
                            all_results["summary"]["successfully_fixed"] += 1
                            all_results["summary"]["total_fixes"] += fix_result.fixed_count
                        else:
                            self.log(f"      ⚠️ 未修复: {fix_result.error_message or '未知错误'}")
                            lang_results["summary"]["failed"] += 1
                            all_results["summary"]["failed"] += 1

                    except Exception as e:
                        self.log(f"      ❌ 在文件修复过程中发生异常: {str(e)}")
                        import traceback
                        traceback.print_exc()

                        lang_results["summary"]["failed"] += 1
                        all_results["summary"]["failed"] += 1

                        all_results["fixed_files"].append({
                            "file": filename,
                            "content": original_file.get("content"),
                            "language": lang_name,
                            "original_content": original_file.get("content"),
                            "fixed_count": 0,
                            "method": "none",
                            "status": "error",
                            "success": False,
                            "error_message": str(e)
                        })

                all_results["by_language"][lang_name] = lang_results
                all_results["summary"]["total_files"] += len(files_to_fix)

                self.log(
                    f"\n   ✅ {lang_name.upper()} 修复完成: {lang_results['summary']['success']} 成功, {lang_results['summary']['failed']} 失败。")

            except Exception as e:
                self.log(f"   ❌ 在为语言 {lang_name.upper()} 设置修复器时发生严重错误: {str(e)}")
                import traceback
                traceback.print_exc()

        self.log(f"\n{'=' * 60}")
        self.log(f"📊 总体修复统计：")
        self.log(f"   - 处理文件: {all_results['summary']['total_files']} 个")
        self.log(f"   - 成功修复: {all_results['summary']['successfully_fixed']} 个")
        self.log(f"   - 修复失败: {all_results['summary']['failed']} 个")
        self.log(f"   - 总修复数: {all_results['summary']['total_fixes']} 处")
        self.log(f"   - fixed_files 列表总数: {len(all_results['fixed_files'])} 个")

        print(f"\n🔥🔥🔥 [DEBUG] execute() 完成，最终 fixed_files 数量: {len(all_results['fixed_files'])}")

        return all_results