"""
OrchestratorAgent - 多语言Bug修复系统的总协调器
"""
import sys
import os
from typing import Dict, Any, List
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .base_agent import BaseAgent
from .scanner_agent import ScannerAgent
from .analyzer_agent import AnalyzerAgent
from .fixer_agent import FixerAgent
from .verifier_agent import VerifierAgent


class OrchestratorAgent(BaseAgent):
    """总协调器Agent - 协调多语言Bug修复流程"""

    def __init__(self, config: Dict[str, Any] = None):
        super().__init__("OrchestratorAgent", config or {})

        # 初始化子Agent
        self.scanner = ScannerAgent(config.get("scanner", {}) if config else {})
        self.analyzer = AnalyzerAgent(config.get("analyzer", {}) if config else {})
        self.fixer = FixerAgent(config.get("fixer", {}) if config else {})
        self.verifier = VerifierAgent(config.get("verifier", {}) if config else {})

        self.workflow_state = {}

    def perceive(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """感知阶段：接收用户输入"""
        files = input_data.get("files", [])
        user_request = input_data.get("user_request", "")
        test_cases = input_data.get("test_cases", [])

        self.log("=" * 80)
        self.log("🚀 多语言Bug检测与修复系统启动")
        self.log("=" * 80)
        self.log(f"\n📂 收到文件: {len(files)} 个")
        for f in files[:20]:  # 只显示前20个
            self.log(f"   - {f.get('file', 'unknown')}")
        if len(files) > 20:
            self.log(f"   ... 还有 {len(files) - 20} 个文件")

        if user_request:
            self.log(f"\n📝 用户需求: {user_request}")

        if test_cases:
            self.log(f"\n🧪 测试用例: {len(test_cases)} 个")

        return {
            "files": files,
            "user_request": user_request,
            "test_cases": test_cases,
            "enable_scanner": self.config.get("enable_scanner", True),
            "enable_analyzer": self.config.get("enable_analyzer", True),
            "enable_fixer": self.config.get("enable_fixer", True),
            "enable_verifier": self.config.get("enable_verifier", True),
        }

    def decide(self, perception: Dict[str, Any]) -> Dict[str, Any]:
        """决策阶段：制定执行计划"""
        strategy = {
            "workflow": [],
            "enable_agents": {}
        }

        # 构建工作流
        if perception.get("enable_scanner", True):
            strategy["workflow"].append("scan")
            strategy["enable_agents"]["scanner"] = True

        if perception.get("enable_analyzer", True):
            strategy["workflow"].append("analyze")
            strategy["enable_agents"]["analyzer"] = True

        if perception.get("enable_fixer", True):
            strategy["workflow"].append("fix")
            strategy["enable_agents"]["fixer"] = True

        if perception.get("enable_verifier", True):
            strategy["workflow"].append("verify")
            strategy["enable_agents"]["verifier"] = True

        self.log(f"\n📋 执行计划：{' -> '.join(strategy['workflow'])}")

        return strategy

    def execute(self, decision: Dict[str, Any]) -> Dict[str, Any]:
        """执行阶段：协调各Agent执行"""
        workflow = decision.get("workflow", [])
        enable_agents = decision.get("enable_agents", {})

        # 初始化结果
        pipeline_results = {
            "scan_results": None,
            "analysis": None,
            "fix_results": None,
            "verification": None,
            "execution_time": {},
            "success": False
        }

        files = decision.get("files", [])
        user_request = decision.get("user_request", "")
        test_cases = decision.get("test_cases", [])

        try:
            # 1. 扫描阶段
            if "scan" in workflow and enable_agents.get("scanner"):
                self.log(f"\n{'=' * 80}")
                self.log("🔍 阶段 1/4：代码扫描")
                self.log("=" * 80)

                start_time = time.time()

                scan_input = {"files": files}
                scan_perception = self.scanner.perceive(scan_input)
                scan_decision = self.scanner.decide(scan_perception)
                # 合并 files 等数据
                scan_decision.update(scan_perception)

                scan_results = self.scanner.execute(scan_decision)

                pipeline_results["scan_results"] = scan_results
                pipeline_results["execution_time"]["scan"] = time.time() - start_time

                self.log(f"\n⏱️ 扫描耗时: {pipeline_results['execution_time']['scan']:.2f}秒")

            # 2. 分析阶段
            if "analyze" in workflow and enable_agents.get("analyzer") and pipeline_results["scan_results"]:
                self.log(f"\n{'=' * 80}")
                self.log("📊 阶段 2/4：问题分析")
                self.log("=" * 80)

                start_time = time.time()

                analyze_input = {
                    "scan_results": pipeline_results["scan_results"],
                    "files": files
                }
                analyze_perception = self.analyzer.perceive(analyze_input)
                analyze_decision = self.analyzer.decide(analyze_perception)
                analyze_decision.update(analyze_perception)

                analysis = self.analyzer.execute(analyze_decision)

                pipeline_results["analysis"] = analysis
                pipeline_results["execution_time"]["analyze"] = time.time() - start_time

                self.log(f"\n⏱️ 分析耗时: {pipeline_results['execution_time']['analyze']:.2f}秒")

            # 3. 修复阶段
            # ✅ 不再用 truthy 判断拦截，而是只要 fixer 启用就运行；
            #    analysis 可能是 None 或 {}，FixerAgent 内部有 DebugBench 兜底逻辑。
            analysis_data = pipeline_results.get("analysis") or {}

            if "fix" in workflow and enable_agents.get("fixer"):
                self.log(f"\n{'=' * 80}")
                self.log("🔧 阶段 3/4：代码修复")
                self.log("=" * 80)

                start_time = time.time()

                fix_input = {
                    "analysis": analysis_data,
                    "files": files,
                    "user_request": user_request
                }
                fix_perception = self.fixer.perceive(fix_input)
                fix_decision = self.fixer.decide(fix_perception)
                fix_decision.update(fix_perception)

                fix_results = self.fixer.execute(fix_decision)

                pipeline_results["fix_results"] = fix_results
                pipeline_results["execution_time"]["fix"] = time.time() - start_time

                self.log(f"\n⏱️ 修复耗时: {pipeline_results['execution_time']['fix']:.2f}秒")

            # 4. 验证阶段
            if "verify" in workflow and enable_agents.get("verifier") and pipeline_results["fix_results"]:
                self.log(f"\n{'=' * 80}")
                self.log("✅ 阶段 4/4：修复验证")
                self.log("=" * 80)

                start_time = time.time()

                verify_input = {
                    "fix_results": pipeline_results["fix_results"],
                    "original_files": files,
                    "original_analysis": pipeline_results["analysis"],
                    "test_cases": test_cases
                }
                verify_perception = self.verifier.perceive(verify_input)
                verify_decision = self.verifier.decide(verify_perception)
                verify_decision.update(verify_perception)

                verification = self.verifier.execute(verify_decision)

                pipeline_results["verification"] = verification
                pipeline_results["execution_time"]["verify"] = time.time() - start_time

                self.log(f"\n⏱️ 验证耗时: {pipeline_results['execution_time']['verify']:.2f}秒")

            pipeline_results["success"] = True

        except Exception as e:
            self.log(f"\n❌ 执行过程中发生错误: {str(e)}")
            import traceback
            error_trace = traceback.format_exc()
            self.log(f"\n错误详情:\n{error_trace}")
            pipeline_results["error"] = str(e)
            pipeline_results["success"] = False

        # 生成总结
        self._generate_summary(pipeline_results)

        return pipeline_results

    def _generate_summary(self, results: Dict[str, Any]):
        """生成执行总结"""
        exec_time = results.get("execution_time", {})
        total_time = sum(exec_time.values())

        self.log("")
        self.log("=" * 80)
        self.log("📊 执行总结")
        self.log("=" * 80)

        self.log("")
        self.log(f"⏱️ 总耗时: {total_time:.2f}秒")

        if total_time > 0:
            for stage, duration in exec_time.items():
                percentage = (duration / total_time * 100)
                self.log(f"   - {stage}: {duration:.2f}秒 ({percentage:.1f}%)")
        else:
            for stage, duration in exec_time.items():
                self.log(f"   - {stage}: {duration:.2f}秒")

        # 扫描结果
        scan_results = results.get("scan_results", {}) or {}
        scan_summary = scan_results.get("summary", {}) or {}

        self.log("")
        self.log("🔍 扫描结果:")
        self.log(f"   - 发现问题: {scan_summary.get('total_defects', 0)} 个")

        by_severity = scan_summary.get("by_severity", {}) or {}
        self.log(f"   - 高危: {by_severity.get('HIGH', 0)} 个")
        self.log(f"   - 中危: {by_severity.get('MEDIUM', 0)} 个")
        self.log(f"   - 低危: {by_severity.get('LOW', 0)} 个")

        # 修复结果
        fix_results = results.get("fix_results", {}) or {}
        fix_summary = fix_results.get("summary", {}) or {}

        self.log("")
        self.log("🔧 修复结果:")
        self.log(f"   - 处理文件: {fix_summary.get('total_files', 0)} 个")
        self.log(f"   - 成功修复: {fix_summary.get('successfully_fixed', 0)} 个")
        self.log(f"   - 修复失败: {fix_summary.get('failed', 0)} 个")
        self.log(f"   - 总修复数: {fix_summary.get('total_fixes', 0)} 处")


def run_multi_language_repair(files: List[Dict],
                              user_request: str = "",
                              test_cases: List[Dict] = None,
                              llm_client=None) -> Dict[str, Any]:
    """
    运行多语言Bug修复流程的便捷函数

    Args:
        files: 文件列表 [{"file": "xxx", "content": "..."}, ...]
        user_request: 用户额外需求
        test_cases: 测试用例
        llm_client: LLM客户端

    Returns:
        完整的执行结果
    """
    config = {
        "fixer": {
            "llm_client": llm_client,
            "use_rules": True,
            "use_llm": llm_client is not None,
            # 🔥 为 Java 启用“无 issue 也尝试 LLM 修复”的兜底策略
            "force_llm_on_empty": {"java": True},
        }
    }

    orchestrator = OrchestratorAgent(config)

    input_data = {
        "files": files,
        "user_request": user_request,
        "test_cases": test_cases or []
    }

    perception = orchestrator.perceive(input_data)
    decision = orchestrator.decide(perception)
    decision.update(perception)
    results = orchestrator.execute(decision)

    return results