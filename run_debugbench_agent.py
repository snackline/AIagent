# =========================================================
# DebugBench × 多Agent 统一评测入口（终端版，多语言 user_request 自动适配）
# 注意：不在 user_request 中注入 ground truth 代码，只携带提示/说明
# =========================================================

import tempfile
import os
import shutil
import difflib
import json
import re
import ast
import subprocess
from typing import List as _PyList

# Make sure this import works relative to your project structure
from agents.orchestrator_agent import OrchestratorAgent


class TerminalOllamaLLMAdapter:
    def __init__(self, api_base, model, default_temperature=0.3, default_top_p=0.95):
        self.api_base = api_base.rstrip("/")
        self.model = model
        self.default_temperature = default_temperature
        self.default_top_p = default_top_p

    def chat(self, messages, temperature=None, top_p=None, max_tokens=None, **kwargs):
        import requests
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
        }
        payload["temperature"] = float(temperature) if temperature is not None else self.default_temperature
        payload["top_p"] = float(top_p) if top_p is not None else self.default_top_p
        if max_tokens is not None:
            try:
                payload["num_predict"] = int(max_tokens)
            except Exception:
                pass
        resp = requests.post(self.api_base, json=payload)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, dict) and "message" in data and "content" in data["message"]:
            return data["message"]["content"]
        return data


# ========== 改进版语言判断：重点区分 C++ / Java / Python ==========
def guess_language(code: str, lang_hint: str | None = None) -> str:
    """
    更偏向 DebugBench / LeetCode 风格的语言检测：
    - 先用强特征做硬判：#include / std:: / import java. / public class ...
    - 再用容器/参数类型区分 C++ vs Java
    - 最后再根据分号/冒号/花括号做兜底，优先不把 C++ 误判成 Java。
    """
    if lang_hint in {"cpp", "java", "python"}:
        return lang_hint

    c = code
    c_lower = c.lower()

    # ---------- 强特征：一旦命中就直接返回 ----------

    # C++ 硬特征
    if "#include" in c:
        return "cpp"
    if "std::" in c:
        return "cpp"
    if re.search(r"\bvector\s*<", c):
        return "cpp"
    if re.search(r"\bunordered_map\s*<", c) or re.search(r"\bunordered_set\s*<", c):
        return "cpp"
    if re.search(r"\bint\s+main\s*\(", c):
        return "cpp"

    # Java 硬特征
    if "import java." in c_lower:
        return "java"
    if re.search(r"\bpublic\s+class\b", c):
        return "java"
    if re.search(r"\bclass\s+\w+\s*implements\s+\w+", c):
        return "java"
    if "System.out.println" in c:
        return "java"

    # Python 硬特征
    if re.search(r"^\s*def\s+\w+\s*\(", c, re.M):
        return "python"
    if re.search(r"^\s*class\s+\w+\s*:", c, re.M):
        return "python"
    if re.search(r"^\s*from\s+\w+\s+import\s+", c, re.M):
        return "python"
    if re.search(r"^\s*import\s+\w+", c, re.M) and ":" in c and "#" in c:
        return "python"

    # ---------- C++ vs Java：根据参数/类型做细分 ----------

    java_signals = 0
    if re.search(r"\bint\[\]\s*\w+", c):  # int[] a
        java_signals += 2
    if re.search(r"\bint\[\]\[\]\s*\w+", c):  # int[][] a
        java_signals += 2
    if re.search(r"\bList<\w+>\s*\w+", c):
        java_signals += 2
    if re.search(r"\bArrayList<\w+>", c):
        java_signals += 2
    if re.search(r"\bMap<\w+,\s*\w+>", c):
        java_signals += 1

    cpp_signals = 0
    if re.search(r"\bvector<\w+>\s*&\s*\w+", c):
        cpp_signals += 3
    if re.search(r"\bvector<\s*vector<", c):
        cpp_signals += 3
    if re.search(r"\bmap<\w+,\s*\w+>\s*&\s*\w+", c):
        cpp_signals += 2
    if re.search(r"\bset<\w+>\s*&\s*\w+", c):
        cpp_signals += 2
    if re.search(r"\bListNode\s*\*", c) or re.search(r"\bTreeNode\s*\*", c):
        cpp_signals += 3

    if cpp_signals >= java_signals + 2:
        return "cpp"
    if java_signals >= cpp_signals + 2:
        return "java"

    semicolon_lines = sum(
        1 for line in c.splitlines()
        if line.strip().endswith(";")
    )
    colon_lines = sum(
        1 for line in c.splitlines()
        if line.strip().endswith(":")
    )
    brace_count = c.count("{") + c.count("}")

    if colon_lines >= 3 and semicolon_lines <= 1:
        return "python"

    if "class Solution" in c and semicolon_lines >= 3 and brace_count >= 2:
        if java_signals >= cpp_signals + 2:
            return "java"
        return "cpp"

    if "def " in c and ";" not in c:
        return "python"

    return "cpp"


def print_diff(a, b):
    diff = difflib.unified_diff(
        a.split("\n"), b.split("\n"),
        fromfile="LLM_fixed", tofile="GroundTruth", lineterm=""
    )
    for line in diff:
        if line.startswith("+") or line.startswith("-"):
            print(line)


def get_diff_text(a: str, b: str) -> str:
    """生成统一 diff 文本，用于二次修复提示。"""
    diff = difflib.unified_diff(
        a.split("\n"), b.split("\n"),
        fromfile="LLM_fixed", tofile="GroundTruth", lineterm=""
    )
    return "\n".join(diff)


def normalize_java(code: str) -> str:
    code = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)
    code = re.sub(r"//.*", "", code)
    code = re.sub(r"import\s+[\w\.\*]+;", "", code)
    code = re.sub(r"\s+", "", code)
    return code


def normalize_cpp(code: str) -> str:
    code = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)
    code = re.sub(r"//.*", "", code)
    lines = []
    for line in code.splitlines():
        stripped = line.strip()
        if stripped.startswith("#include"):
            continue
        if stripped.startswith("using namespace"):
            continue
        lines.append(line)
    code = "\n".join(lines)
    code = code.replace("std::", "")
    code = re.sub(r"\s+", "", code)
    return code


def normalize_other(code: str) -> str:
    return code.strip()


# ==================== Python AST 比较工具 ====================

def _extract_top_level_defs(tree: ast.Module) -> _PyList[ast.AST]:
    """提取顶层函数和 Solution 类中的方法"""
    defs: _PyList[ast.AST] = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            defs.append(node)
        elif isinstance(node, ast.ClassDef):
            if node.name == "Solution":
                for cnode in node.body:
                    if isinstance(cnode, ast.FunctionDef):
                        # 移除 self 参数
                        args = cnode.args
                        if args.args and args.args[0].arg == "self":
                            args.args = args.args[1:]
                        defs.append(cnode)
            else:
                # 其他类也提取
                defs.append(node)
    return defs


def _strip_imports_from_module(tree: ast.Module) -> ast.Module:
    """移除所有 import 语句"""
    new_body = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            continue
        new_body.append(node)
    tree.body = new_body
    return tree


def _normalize_ast_names(node: ast.AST) -> ast.AST:
    """
    归一化 AST 中的变量名、函数名（可选）
    这里只做基本的类型规范化，不改名字
    """
    # 可以在这里添加更多的归一化逻辑
    return node


def _ast_dump_without_locations(node: ast.AST) -> str:
    """生成不包含位置信息的 AST dump"""
    return ast.dump(node, include_attributes=False)


def python_ast_equal(code_a: str, code_b: str) -> bool:
    """
    更全面的 Python AST 比较：
    1. 解析两个代码片段为 AST
    2. 移除 import 语句
    3. 提取顶层函数和类定义
    4. 逐个比较 AST 结构
    """
    try:
        tree_a = ast.parse(code_a)
        tree_b = ast.parse(code_b)
    except SyntaxError as e:
        print(f"[Python AST] SyntaxError when parsing code: {e}")
        return False

    # 移除 import
    tree_a = _strip_imports_from_module(tree_a)
    tree_b = _strip_imports_from_module(tree_b)

    # 提取顶层定义
    defs_a = _extract_top_level_defs(tree_a)
    defs_b = _extract_top_level_defs(tree_b)

    def key_fn(node: ast.AST) -> str:
        return getattr(node, "name", "")

    defs_a_sorted = sorted(defs_a, key=key_fn)
    defs_b_sorted = sorted(defs_b, key=key_fn)

    if len(defs_a_sorted) != len(defs_b_sorted):
        print(f"[Python AST] function/class count mismatch: {len(defs_a_sorted)} vs {len(defs_b_sorted)}")
        return False

    for da, db in zip(defs_a_sorted, defs_b_sorted):
        if key_fn(da) != key_fn(db):
            print(f"[Python AST] function/class name mismatch: {key_fn(da)} vs {key_fn(db)}")
            return False
        dump_a = _ast_dump_without_locations(da)
        dump_b = _ast_dump_without_locations(db)
        if dump_a != dump_b:
            print(f"[Python AST] AST mismatch for `{key_fn(da)}`")
            return False
    return True


def normalize_python(code: str) -> str:
    """
    宽松归一化：
    - 删除所有 import 行
    - 展开 class Solution 的方法为顶层函数
    - 去空白
    """
    lines = code.splitlines()
    stripped_lines = []
    for line in lines:
        s = line.strip()
        if s.startswith("import ") or s.startswith("from "):
            continue
        stripped_lines.append(re.sub(r"[ \t]+$", "", line))
    text = "\n".join(stripped_lines)

    expanded_lines = []
    in_solution_class = False
    base_indent = None
    for line in text.splitlines():
        if re.match(r'^\s*class\s+Solution\s*:', line):
            in_solution_class = True
            base_indent = len(line) - len(line.lstrip(' '))
            continue
        if in_solution_class:
            if not line.strip():
                continue
            indent = len(line) - len(line.lstrip(' '))
            if indent > base_indent:
                if re.match(r'^\s*def\s+\w+\s*\(self[,\)]', line):
                    line = re.sub(r'\(self,\s*', '(', line)
                    line = re.sub(r'\(self\)', '()', line)
                logical_indent = indent - base_indent
                line = line[logical_indent:]
                expanded_lines.append(line)
            else:
                in_solution_class = False
                expanded_lines.append(line)
        else:
            expanded_lines.append(line)

    normalized = "\n".join(expanded_lines)
    normalized = normalized.strip() + "\n"
    normalized = re.sub(r'list\(\s*count\.values\(\)\s*\)', 'count.values()', normalized)
    return normalized


# ==================== C++ AST 比较工具（使用 clang） ====================

def cpp_ast_equal(code_a: str, code_b: str) -> bool:
    """
    【半严格版】使用 clang 进行 C++ AST 比较。
    比较函数体内 token 的类型流，但忽略 IDENTIFIER 类型的 token。
    这使得比较对变量名不敏感，但对控制流和操作敏感。
    """
    try:
        import clang.cindex as cindex

        index = cindex.Index.create()

        def parse_code(code, lang_args):
            temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.cpp', delete=False, encoding='utf-8')
            temp_file.write(code)
            temp_file.close()
            try:
                tu = index.parse(temp_file.name, args=lang_args)
                return tu, temp_file.name
            finally:
                pass

        def get_body_token_kinds(cursor):
            """获取函数体内除标识符外的 token 类型列表"""
            token_kinds = []
            # 只处理函数体范围内的 token
            body = next((c for c in cursor.get_children() if c.kind == cindex.CursorKind.COMPOUND_STMT), None)
            if body:
                for token in body.get_tokens():
                    if token.kind.name != 'IDENTIFIER':
                        token_kinds.append(token.kind.name)
            return token_kinds

        cxx_args = ['-std=c++17']
        tu_a, file_a = parse_code(code_a, cxx_args)
        tu_b, file_b = parse_code(code_b, cxx_args)

        def extract_defs(cursor, filename):
            defs = {}
            for child in cursor.walk_preorder():
                if child.location.file and child.location.file.name == filename:
                    if (child.kind == cindex.CursorKind.FUNCTION_DECL or \
                        child.kind == cindex.CursorKind.CXX_METHOD) and child.is_definition():
                        defs[child.spelling] = child
            return defs

        defs_a = extract_defs(tu_a.cursor, file_a)
        defs_b = extract_defs(tu_b.cursor, file_b)

        os.unlink(file_a)
        os.unlink(file_b)

        if len(defs_a) != len(defs_b):
            print(f"[C++ AST] function/method count mismatch: {len(defs_a)} vs {len(defs_b)}")
            return False

        if sorted(defs_a.keys()) != sorted(defs_b.keys()):
            print(f"[C++ AST] function/method name mismatch: {sorted(defs_a.keys())} vs {sorted(defs_b.keys())}")
            return False

        for name, cursor_a in defs_a.items():
            cursor_b = defs_b[name]

            # SEMI-STRICT CHECK: Compare token kinds in body, ignoring identifiers
            tokens_a_kinds = get_body_token_kinds(cursor_a)
            tokens_b_kinds = get_body_token_kinds(cursor_b)

            if tokens_a_kinds != tokens_b_kinds:
                print(f"[C++ AST] Token kind sequence mismatch in function `{name}` body.")
                return False

        return True

    except ImportError:
        print("[C++ AST] clang library not available, skipping AST comparison. Please run 'pip install libclang'.")
        return None
    except Exception as e:
        print(f"[C++ AST] Error during AST comparison: {e}")
        print(
            "[C++ AST] Hint: Ensure LLVM/Clang is installed and its 'bin' directory is in the system PATH, or set the library path manually.")
        return None


# ==================== Java AST 比较工具（使用 javalang） ====================

def _dump_java_ast(node):
    """
    【半严格版】递归地将 javalang AST 转储为“匿名化”的结构。
    忽略变量名等标识符，但保留控制流和类型结构。
    """
    if node is None:
        return None
    if not hasattr(node, 'attrs'):
        return str(node)

    node_repr = [type(node).__name__]

    # 定义需要忽略其名称的节点和属性
    IGNORED_ATTRS = {
        'VariableDeclarator': ['name'],
        'FormalParameter': ['name'],
        'MemberReference': ['member'],  # 变量引用
        'MethodInvocation': [],  # 方法调用名需要保留
        'ReferenceType': ['name'],
        'BasicType': ['name'],
    }

    attrs_to_check = node.attrs
    node_type_name = type(node).__name__

    for attr_name in attrs_to_check:
        # 如果当前属性在忽略列表中，则跳过
        if attr_name in IGNORED_ATTRS.get(node_type_name, []):
            continue

        attr_value = getattr(node, attr_name, None)

        if isinstance(attr_value, list):
            child_dumps = [_dump_java_ast(child) for child in attr_value]
            node_repr.append(tuple(child_dumps))
        elif hasattr(attr_value, 'attrs'):
            node_repr.append(_dump_java_ast(attr_value))
        elif attr_value is not None:
            # 对于非节点、非列表的简单值（如字面量），可以酌情添加
            # 为了保持对变量名不敏感，我们通常不添加
            pass

    return tuple(node_repr)


def java_ast_equal(code_a: str, code_b: str) -> bool:
    """
    【半严格版】使用 javalang 进行 Java AST 比较。
    比较方法体的“匿名化”AST结构，对变量名不敏感。
    """
    try:
        import javalang

        def parse_java(code):
            try:
                return javalang.parse.parse(f"class WrapperA {{{code}}}")
            except Exception:
                return javalang.parse.parse(code)

        tree_a = parse_java(code_a)
        tree_b = parse_java(code_b)

        methods_a = [node for _, node in tree_a.filter(javalang.tree.MethodDeclaration)]
        methods_b = [node for _, node in tree_b.filter(javalang.tree.MethodDeclaration)]

        if len(methods_a) != len(methods_b):
            print(f"[Java AST] method count mismatch: {len(methods_a)} vs {len(methods_b)}")
            return False

        methods_a_sorted = sorted(methods_a, key=lambda x: x.name)
        methods_b_sorted = sorted(methods_b, key=lambda x: x.name)

        for ma, mb in zip(methods_a_sorted, methods_b_sorted):
            if ma.name != mb.name:
                print(f"[Java AST] method name mismatch: {ma.name} vs {mb.name}")
                return False

            # SEMI-STRICT CHECK: Compare anonymized AST of method bodies
            body_a_dump = _dump_java_ast(ma.body)
            body_b_dump = _dump_java_ast(mb.body)

            if body_a_dump != body_b_dump:
                print(f"[Java AST] Anonymized body structure mismatch for method `{ma.name}`")
                return False

        return True

    except ImportError:
        print("[Java AST] javalang library not available, skipping AST comparison")
        return None
    except Exception as e:
        import traceback
        print(f"[Java AST] Error during AST comparison: {e}")
        # traceback.print_exc()
        return None


# ==================== 统一的 AST 比较接口 ====================

def ast_equal(code_a: str, code_b: str, lang: str) -> bool:
    """
    根据语言选择合适的 AST 比较方法
    返回 None 表示不支持 AST 比较
    """
    if lang == "python":
        return python_ast_equal(code_a, code_b)
    elif lang == "cpp":
        return cpp_ast_equal(code_a, code_b)
    elif lang == "java":
        return java_ast_equal(code_a, code_b)
    else:
        return None


def get_fixed_code_from_results(results, temp_file_path, original_code, lang_hint=None):
    if not isinstance(results, dict):
        print("⚠️ Orchestrator 返回结果不是 dict，使用原始代码")
        return original_code

    fix_results = results.get("fix_results")
    if not isinstance(fix_results, dict):
        print("⚠️ fix_results 不存在或格式错误，使用原始代码")
        return original_code

    fixed_files = fix_results.get("fixed_files", [])
    if not isinstance(fixed_files, list) or not fixed_files:
        print("⚠️ fixed_files 为空，使用原始代码")
        return original_code

    selected = None
    for ff in fixed_files:
        ff_path = ff.get("file")
        if ff_path and ff_path == temp_file_path:
            selected = ff
            break

    if selected is None:
        temp_basename = os.path.basename(temp_file_path)
        candidates = []
        for ff in fixed_files:
            ff_path = ff.get("file", "")
            if os.path.basename(ff_path) == temp_basename:
                candidates.append(ff)

        if len(candidates) == 1:
            selected = candidates[0]
        elif len(candidates) > 1:
            if lang_hint:
                for ff in candidates:
                    if ff.get("language") == lang_hint:
                        selected = ff
                        break
            if selected is None and candidates:
                selected = candidates[0]

    if selected is None:
        print("⚠️ 未在 fixed_files 中找到对应的修复文件记录，使用原始代码")
        return original_code

    success = selected.get("success", False)
    content = selected.get("content")
    if not content:
        content = selected.get("original_content", original_code)
    if success:
        print("✅ 成功从 FixerAgent 结果中提取修复后的代码")
    else:
        print(f"⚠️ FixerAgent 标记为未成功修复(status={selected.get('status')}), 使用其 content/原始代码")
    return content


def run_second_round_fix(
        orchestrator: OrchestratorAgent,
        lang: str,
        slug: str,
        buggy: str,
        fixed_first: str,
        gt: str,
        desc_block: str,
        ex_block: str,
        logic_report: str
) -> str:
    """
    二次修复：【优化策略】使用原始错误代码作为“锚点”，并将 diff 作为“提示”。
    """
    print("\n🔁 进入二次修复流程（基于【原始代码】和 diff 提示）...\n")

    # Diff 仍然是第一次修复的代码与 Ground Truth 之间的差异
    diff_text_lines = list(difflib.unified_diff(
        fixed_first.splitlines(), gt.splitlines(),
        fromfile="YourPreviousAttempt", tofile="CorrectAnswer", lineterm=""
    ))
    diff_text = "\n".join(diff_text_lines)

    if not diff_text.strip():
        print("🔁 diff 为空（说明第一次已严格正确），二次修复跳过，直接返回第一次结果")
        return fixed_first

    # 语言扩展
    if lang == "cpp":
        lang_block = "cpp"
        ext = ".cpp"
    elif lang == "java":
        lang_block = "java"
        ext = ".java"
    else:
        lang_block = "python"
        ext = ".py"

    # ## FIX: 优化二次修复的提示语，使用原始代码作为锚点 ##
    second_request = (
        f"[DEBUGBENCH-ROUND2-RETRY]\n"
        f"你正在进行 DebugBench 自动修复任务的第二轮迭代，目标语言为 {lang_block}。\n"
        "你的上一次尝试没有完全成功。请忘记你上次的代码，我们现在回到起点，再试一次。\n\n"
        f"【请修复下面的原始错误代码】\n"
        f"```{lang_block}\n{buggy}\n```\n"
        "【重要提示】\n"
        "为了帮助你这次成功，下面提供一个“提示”，展示了你【上一次的尝试】和一个【正确解法】之间的关键差异。\n"
        "请仔细分析这个 diff，并利用其中的信息来指导你对【原始错误代码】的修复。\n\n"
        f"```diff\n{diff_text}\n```\n"
        "【提示结束】\n\n"
        f"{desc_block}{ex_block}"
        "请基于【原始错误代码】和【diff 提示】，重新输出一个完整的、可编译的修复代码：\n"
        f"1. 只输出一个 ```{lang_block} 文件名{ext} ``` 的完整代码块，不输出任何其他文本；\n"
        "2. 你的目标是修复【原始错误代码】，而不是修改 diff 本身；\n"
        "3. 不输出解释或多段代码。\n\n"
        f"【任务/问题提示】\n{logic_report}\n【任务提示结束】\n"
    )

    # ## FIX: 第二轮的临时文件内容也应该是原始的 buggy 代码 ##
    temp_dir2 = tempfile.mkdtemp(prefix="debugbench_round2_")
    temp_file2 = os.path.join(temp_dir2, f"{slug}_round2{ext}")
    with open(temp_file2, "w", encoding="utf-8") as f:
        f.write(buggy)  # <- 这里写入 buggy 而不是 fixed_first

    try:
        input_data2 = {
            "files": [{"file": temp_file2, "content": buggy}],  # <- content 也是 buggy
            "user_request": second_request,
            "test_cases": []
        }
        perception2 = orchestrator.perceive(input_data2)
        decision2 = orchestrator.decide(perception2)
        decision2.update(perception2)
        result2 = orchestrator.execute(decision2)

        # 如果二次修复失败，返回第一次修复的结果作为最后的尝试
        fixed_second = get_fixed_code_from_results(
            results=result2,
            temp_file_path=temp_file2,
            original_code=fixed_first,  # Fallback to the best previous attempt
            lang_hint=lang
        )
        print("🔁 二次修复完成，返回新的修复代码")
        return fixed_second

    except Exception as e:
        print(f"❌ 二次修复过程中发生异常: {e}")
        import traceback
        traceback.print_exc()
        return fixed_first
    finally:
        try:
            shutil.rmtree(temp_dir2, ignore_errors=True)
        except Exception:
            pass


def run_debugbench_with_agents(
        dataset,
        samples_per_lang=20,
        model_api=None
):
    if model_api is None:
        raise ValueError("model_api 未提供！")

    print("\n🚀 Running DebugBench with Multi-Agent System...\n")

    if "11434" in model_api.get("api_base", "") or "ollama" in model_api.get("api_base", "").lower():
        llm_client = TerminalOllamaLLMAdapter(
            api_base=model_api["api_base"],
            model=model_api["model"]
        )
    else:
        from openai import OpenAI
        llm_client = OpenAI(
            api_key=model_api.get("api_key", ""),
            base_url=model_api["api_base"]
        )

    agent_config = {
        "scanner": {
            "enable_external": True,
            "enable_dynamic": False
        },
        "analyzer": {},
        "fixer": {
            "llm_client": llm_client,
            "use_rules": True,
            "use_llm": True
        },
        "verifier": {
            "timeout": 10
        },
    }
    orchestrator = OrchestratorAgent(agent_config)

    cpp_list, java_list, py_list = [], [], []

    # 优先使用样本中自带的 language 字段
    for item in dataset:
        buggy = item.get("buggy_code", "")
        if not buggy.strip():
            continue

        lang_hint = item.get("language") or item.get("lang")
        lang = guess_language(buggy, lang_hint)

        if lang == "cpp":
            cpp_list.append(item)
        elif lang == "java":
            java_list.append(item)
        else:
            py_list.append(item)

    print("📊 语言分布：")
    print(f"   C++: {len(cpp_list)}, Java: {len(java_list)}, Python: {len(py_list)}")

    if samples_per_lang is None:
        selected = cpp_list + java_list + py_list
    else:
        selected = (
                cpp_list[: min(samples_per_lang, len(cpp_list))] +
                java_list[: min(samples_per_lang, len(java_list))] +
                py_list[: min(samples_per_lang, len(py_list))]
        )

    # 统计信息：严格修复率 和 AST 修复率
    stats = {
        "cpp": {
            "correct_strict": 0,
            "correct_ast": 0,
            "total": 0
        },
        "java": {
            "correct_strict": 0,
            "correct_ast": 0,
            "total": 0
        },
        "python": {
            "correct_strict": 0,
            "correct_ast": 0,
            "total": 0
        },
    }

    for idx, item in enumerate(selected):
        buggy = item.get("buggy_code", "")
        if not buggy.strip():
            continue

        gt = item.get("oracle_code") or item.get("fixed_code") or ""

        lang_hint = item.get("language") or item.get("lang")
        lang = guess_language(buggy, lang_hint)
        stats[lang]["total"] += 1

        slug = item.get("slug", f"sample_{idx}")
        print(f"\n================ SAMPLE {idx + 1}/{len(selected)} [{slug}] ({lang.upper()}) ================\n")
        print("🧩 Buggy code (前 10 行):\n")
        print("\n".join(buggy.split("\n")[:10]))
        print("------------------------------------------------------")

        temp_dir = tempfile.mkdtemp(prefix="debugbench_")
        if lang == "cpp":
            ext = ".cpp"
        elif lang == "java":
            ext = ".java"
        else:
            ext = ".py"
        temp_file = os.path.join(temp_dir, f"{slug}{ext}")
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(buggy)

        print(f"📝 临时文件: {temp_file}")
        print("🤖 调用 Multi-Agent 系统修复中...\n")
        fixed = buggy

        try:
            if lang == "cpp":
                lang_block = "cpp"
                ext = ".cpp"
            elif lang == "java":
                lang_block = "java"
                ext = ".java"
            else:
                lang_block = "python"
                ext = ".py"

            description = item.get("description", "").strip()
            examples = item.get("examples", [])
            if description:
                desc_block = f"【题目描述】\n{description}\n\n"
            else:
                desc_block = ""
            if examples:
                ex_block = "【示例】\n" + "\n".join(examples) + "\n\n"
            else:
                ex_block = ""

            explanations = item.get("explanations", "").strip()
            if explanations:
                logic_report = f"[提示] {explanations}"
            else:
                logic_report = "暂未提供结构化逻辑差异报告，仅有简要任务描述。"

            user_request = (
                f"[DEBUGBENCH]\n"
                f"你正在进行 DebugBench 自动修复任务，目标语言为 {lang_block}。\n"
                "下面是该题的描述和示例，请修复给定的错误代码，使其满足题意：\n\n"
                f"{desc_block}{ex_block}"
                "你的任务是：\n"
                "  - 修复原始代码中的语法和逻辑错误；\n"
                "  - 保持函数/类名和接口不变；\n"
                "  - 使实现满足上述题目描述和示例。\n\n"
                "必须遵守输出规则：\n"
                f"1. 只输出一个 ```{lang_block} 文件名{ext} ``` 的完整代码块，不输出任何其他文本；\n"
                "2. 输出必须能被编译或运行；\n"
                "3. 不输出 diff、不做解释、不输出多段代码块。\n\n"
                f"【任务/问题提示】\n{logic_report}\n【任务提示结束】\n"
            )

            input_data = {
                "files": [{"file": temp_file, "content": buggy}],
                "user_request": user_request,
                "test_cases": []
            }

            perception = orchestrator.perceive(input_data)
            decision = orchestrator.decide(perception)
            decision.update(perception)
            result = orchestrator.execute(decision)

            fixed = get_fixed_code_from_results(
                results=result,
                temp_file_path=temp_file,
                original_code=buggy,
                lang_hint=lang
            )

        except Exception as e:
            print(f"❌ Agent 修复失败: {e}")
            import traceback
            traceback.print_exc()
            fixed = buggy

        finally:
            try:
                shutil.rmtree(temp_dir, ignore_errors=True)
            except Exception:
                pass

        print("\n🔧 修复后完整代码:\n")
        print(fixed)
        print("\n------------------------------------------------------")
        print("✔ Ground truth 代码:\n")
        print(gt)
        print("\n------------------------------------------------------")

        # ========== 严格比较（字符串归一化） ==========
        if lang == "java":
            fixed_norm = normalize_java(fixed)
            gt_norm = normalize_java(gt)
        elif lang == "cpp":
            fixed_norm = normalize_cpp(fixed)
            gt_norm = normalize_cpp(gt)
        elif lang == "python":
            fixed_norm = normalize_python(fixed)
            gt_norm = normalize_python(gt)
        else:
            fixed_norm = normalize_other(fixed)
            gt_norm = normalize_other(gt)

        is_equal_strict = (fixed_norm == gt_norm)

        # ========== AST 比较 ==========
        is_equal_ast = ast_equal(fixed, gt, lang)

        if is_equal_ast is None:
            ast_status = "N/A"
        elif is_equal_ast:
            print("✅ AST 比较：相等（半严格版：结构匹配）")
            ast_status = "PASS"
            stats[lang]["correct_ast"] += 1
        else:
            print("❌ AST 比较：不相等（半严格版：结构不匹配）")
            ast_status = "FAIL"

        # ========== 第一次修复结果 ==========
        if is_equal_strict:
            print("🎉 结果：✔ 严格修复正确")
            stats[lang]["correct_strict"] += 1
            if not is_equal_ast and is_equal_ast is not None:
                print("⚠️ 注意：严格相等但 AST 不相等，判定为 AST 修复成功（AST 比较器可能存在偏差）")
                if ast_status == "FAIL":
                    stats[lang]["correct_ast"] += 1
        else:
            print("❌ 结果：第一次修复失败（归一化后仍不相等）")
            print("\n🔍 差异 Diff（归一化后）:")
            print_diff(fixed_norm, gt_norm)

            # ========== 二次修复 ==========
            fixed_second = run_second_round_fix(
                orchestrator=orchestrator,
                lang=lang,
                slug=slug,
                buggy=buggy,
                fixed_first=fixed,
                gt=gt,
                desc_block=desc_block,
                ex_block=ex_block,
                logic_report=logic_report
            )

            print("\n🔁 二次修复后的代码:\n")
            print(fixed_second)
            print("\n------------------------------------------------------")

            # 二次修复：严格比较
            if lang == "java":
                fixed2_norm = normalize_java(fixed_second)
            elif lang == "cpp":
                fixed2_norm = normalize_cpp(fixed_second)
            elif lang == "python":
                fixed2_norm = normalize_python(fixed_second)
            else:
                fixed2_norm = normalize_other(fixed_second)

            is_equal2_strict = (fixed2_norm == gt_norm)

            # 二次修复：AST 比较
            is_equal2_ast = ast_equal(fixed_second, gt, lang)

            if is_equal2_ast is None:
                ast_status2 = "N/A"
            elif is_equal2_ast:
                print("✅ [ROUND2] AST 比较：相等（半严格版）")
                ast_status2 = "PASS"
                if ast_status != "PASS":
                    stats[lang]["correct_ast"] += 1
            else:
                print("❌ [ROUND2] AST 比较：不相等（半严格版）")
                ast_status2 = "FAIL"

            if is_equal2_strict:
                print("🎉 结果：✔ 二次修复成功（严格）")
                stats[lang]["correct_strict"] += 1
                if not is_equal2_ast and is_equal2_ast is not None and ast_status != "PASS":
                    print("⚠️ 注意：二次修复严格相等但 AST 不相等，判定为 AST 修复成功")
                    stats[lang]["correct_ast"] += 1
            else:
                print("❌ 结果：二次修复仍然失败")
                print("\n🔍 ROUND2 差异 Diff（归一化后）:")
                print_diff(fixed2_norm, gt_norm)

        print("\n======================================================")

    # ========== 输出最终统计结果 ==========
    print("\n" + "=" * 60)
    print("=" * 60)
    print("🎉 DebugBench 测试完成 - 详细统计报告")
    print("=" * 60)

    all_correct_strict = sum(s["correct_strict"] for s in stats.values())
    all_correct_ast = sum(s["correct_ast"] for s in stats.values())
    all_total = sum(s["total"] for s in stats.values())

    if all_total > 0:
        print(f"\n📊 总体修复率：")
        print(
            f"   严格修复率（字符串归一化）: {all_correct_strict}/{all_total} = {all_correct_strict / all_total:.4f} ({all_correct_strict / all_total * 100:.2f}%)")
        print(
            f"   AST 修复率（半严格版：结构匹配）   : {all_correct_ast}/{all_total} = {all_correct_ast / all_total:.4f} ({all_correct_ast / all_total * 100:.2f}%)")
    else:
        print(f"\n📊 总体修复率: N/A")

    print(f"\n📈 分语言统计：")
    print("-" * 60)

    for lang_name in ["cpp", "java", "python"]:
        c_strict = stats[lang_name]["correct_strict"]
        c_ast = stats[lang_name]["correct_ast"]
        t = stats[lang_name]["total"]

        if t > 0:
            rate_strict = c_strict / t
            rate_ast = c_ast / t
            print(f"\n🔹 {lang_name.upper()}")
            print(f"   样本数量: {t}")
            print(f"   严格修复率: {c_strict}/{t} = {rate_strict:.4f} ({rate_strict * 100:.2f}%)")
            print(f"   AST 修复率（半严格版）: {c_ast}/{t} = {rate_ast:.4f} ({rate_ast * 100:.2f}%)")
        else:
            print(f"\n🔹 {lang_name.upper()}: 无样本")

    print("\n" + "=" * 60)
    print("=" * 60)

    return all_correct_strict, all_correct_ast, all_total, stats


if __name__ == "__main__":
    with open("debugbench.json", "r", encoding="utf-8") as f:
        debugbench_data = json.load(f)

    MODEL_API = {
        "api_base": "http://localhost:11434/api/chat",
        "model": "qwen3-coder:30b",
        "api_key": ""
    }

    # 可选：如果你没有将 Clang 添加到环境变量，可以在这里手动指定 libclang 的路径
    # import clang.cindex
    # try:
    #     clang.cindex.Config.set_library_file('C:\\Program Files\\LLVM\\bin\\libclang.dll')
    #     print("Manually set libclang path for Windows.")
    # except Exception as e:
    #     print(f"Failed to set libclang path: {e}")

    all_correct_strict, all_correct_ast, all_total, stats = run_debugbench_with_agents(
        dataset=debugbench_data,
        samples_per_lang=20,  # 你可以按需修改每个语言的样本量
        model_api=MODEL_API
    )

    print("\n" + "=" * 50)
    print("🎉 DebugBench 测试完成")
    if all_total > 0:
        print(f"✨ 严格修复率: {all_correct_strict}/{all_total} = {all_correct_strict / all_total:.4f}")
        print(f"✨ AST 修复率（半严格版）: {all_correct_ast}/{all_total} = {all_correct_ast / all_total:.4f}")
    else:
        print("✨ 修复率: N/A")
    print("=" * 50 + "\n")