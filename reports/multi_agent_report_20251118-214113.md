# 🧾 Multi-Agent 详细修复报告

**生成时间**：2025-11-18 21:41:13.716354

---

## 🔍 扫描结果（详细）

### 🐛 内置规则缺陷（0 个）

### 🔧 外部工具执行情况

### ⚠️ 动态编译错误


## 📊 分析阶段

内容：
```json
{
  "summary": {
    "total_languages": 1,
    "total_issues": 142,
    "high_priority": 3,
    "medium_priority": 7,
    "low_priority": 132
  },
  "by_language": {
    "python": {
      "total": 142,
      "issues_by_file": {
        "arena.py": [
          {
            "file": "arena.py",
            "line": 12,
            "col": 8,
            "severity": "MEDIUM",
            "rule_id": "PY100",
            "message": "疑似使用了未定义的名称 'super'（可能为动态导入或第三方库）。",
            "snippet": "        super(Arena, self).__init__(250, 255, 255, 255, define.WIDTH, define.HEIGHT)",
            "count": 1,
            "examples": []
          },
          {
            "file": "arena.py",
            "line": 42,
            "col": 8,
            "severity": "LOW",
            "rule_id": "PY010",
            "message": "使用裸 except，建议捕获具体异常类型。",
            "snippet": "        except:",
            "count": 1,
            "examples": []
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 20,
              "row": 6
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import cocos\nfrom cocos.director import director\n\nimport define\nfrom dot import Dot\nfrom snake import (\n    Snake,  # keep original import; note: mismatch with snake_game.py if that's the actual file\n)\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 8
                  },
                  "location": {
                    "column": 1,
                    "row": 1
                  }
                }
              ],
              "message": "Organize imports"
            },
            "location": {
              "column": 1,
              "row": 1
            },
            "message": "Import block is un-sorted or un-formatted",
            "noqa_row": 1,
            "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E501",
            "end_location": {
              "column": 109,
              "row": 5
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
            "fix": null,
            "location": {
              "column": 89,
              "row": 5
            },
            "message": "Line too long (108 > 88)",
            "noqa_row": 5,
            "url": "https://docs.astral.sh/ruff/rules/line-too-long",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E501",
            "end_location": {
              "column": 93,
              "row": 13
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
            "fix": null,
            "location": {
              "column": 89,
              "row": 13
            },
            "message": "Line too long (92 > 88)",
            "noqa_row": 13,
            "url": "https://docs.astral.sh/ruff/rules/line-too-long",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "B007",
            "end_location": {
              "column": 14,
              "row": 22
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
            "fix": {
              "applicability": "unsafe",
              "edits": [
                {
                  "content": "_i",
                  "end_location": {
                    "column": 14,
                    "row": 22
                  },
                  "location": {
                    "column": 13,
                    "row": 22
                  }
                }
              ],
              "message": "Rename unused `i` to `_i`"
            },
            "location": {
              "column": 13,
              "row": 22
            },
            "message": "Loop control variable `i` not used within loop body",
            "noqa_row": 22,
            "url": "https://docs.astral.sh/ruff/rules/unused-loop-control-variable",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "B007",
            "end_location": {
              "column": 14,
              "row": 27
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
            "fix": {
              "applicability": "unsafe",
              "edits": [
                {
                  "content": "_i",
                  "end_location": {
                    "column": 14,
                    "row": 27
                  },
                  "location": {
                    "column": 13,
                    "row": 27
                  }
                }
              ],
              "message": "Rename unused `i` to `_i`"
            },
            "location": {
              "column": 13,
              "row": 27
            },
            "message": "Loop control variable `i` not used within loop body",
            "noqa_row": 27,
            "url": "https://docs.astral.sh/ruff/rules/unused-loop-control-variable",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E722",
            "end_location": {
              "column": 15,
              "row": 42
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
            "fix": null,
            "location": {
              "column": 9,
              "row": 42
            },
            "message": "Do not use bare `except`",
            "noqa_row": 42,
            "url": "https://docs.astral.sh/ruff/rules/bare-except",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 51,
              "row": 59
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 51,
                    "row": 59
                  },
                  "location": {
                    "column": 51,
                    "row": 59
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 51,
              "row": 59
            },
            "message": "No newline at end of file",
            "noqa_row": 59,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "",
            "line": 2,
            "column": 0,
            "endLine": 2,
            "endColumn": 35,
            "path": "arena.py",
            "symbol": "import-error",
            "message": "Unable to import 'cocos.director'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "",
            "line": 2,
            "column": 0,
            "endLine": 2,
            "endColumn": 35,
            "path": "arena.py",
            "symbol": "no-name-in-module",
            "message": "No name 'director' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "Arena",
            "line": 8,
            "column": 12,
            "endLine": 8,
            "endColumn": 23,
            "path": "arena.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'layer' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "Arena.__init__",
            "line": 14,
            "column": 21,
            "endLine": 14,
            "endColumn": 32,
            "path": "arena.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'batch' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.__init__",
            "line": 22,
            "column": 12,
            "endLine": 22,
            "endColumn": 13,
            "path": "arena.py",
            "symbol": "unused-variable",
            "message": "Unused variable 'i'",
            "message-id": "W0612",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.add_enemy",
            "line": 42,
            "column": 8,
            "endLine": 44,
            "endColumn": 16,
            "path": "arena.py",
            "symbol": "bare-except",
            "message": "No exception type(s) specified",
            "message-id": "W0702",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "Arena.update",
            "line": 47,
            "column": 34,
            "endLine": 47,
            "endColumn": 46,
            "path": "arena.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "Arena.update",
            "line": 48,
            "column": 34,
            "endLine": 48,
            "endColumn": 46,
            "path": "arena.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "Arena.update",
            "line": 50,
            "column": 8,
            "endLine": 50,
            "endColumn": 22,
            "path": "arena.py",
            "symbol": "no-member",
            "message": "Instance of 'Arena' has no 'undefined' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.update",
            "line": 46,
            "column": 21,
            "endLine": 46,
            "endColumn": 23,
            "path": "arena.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'dt'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.on_key_press",
            "line": 52,
            "column": 32,
            "endLine": 52,
            "endColumn": 41,
            "path": "arena.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'modifiers'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "Arena.on_key_release",
            "line": 58,
            "column": 8,
            "endLine": 58,
            "endColumn": 33,
            "path": "arena.py",
            "symbol": "no-member",
            "message": "Instance of 'set' has no 'removee' member; maybe 'remove'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.on_key_release",
            "line": 56,
            "column": 35,
            "endLine": 56,
            "endColumn": 44,
            "path": "arena.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'modifiers'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.update",
            "line": 47,
            "column": 8,
            "endLine": 47,
            "endColumn": 14,
            "path": "arena.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'x' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.update",
            "line": 48,
            "column": 8,
            "endLine": 48,
            "endColumn": 14,
            "path": "arena.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'y' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "code": "41             enemy.optional_attr = enemy.nonexistent_attribute\n42         except:\n43             # swallow everything deliberately\n44             pass\n45 \n",
            "col_offset": 8,
            "end_col_offset": 16,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 703,
              "link": "https://cwe.mitre.org/data/definitions/703.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Try, Except, Pass detected.",
            "line_number": 42,
            "line_range": [
              42,
              43,
              44
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b110_try_except_pass.html",
            "test_id": "B110",
            "test_name": "try_except_pass",
            "tool": "bandit"
          }
        ],
        "dot.py": [
          {
            "file": "dot.py",
            "line": 13,
            "col": 24,
            "severity": "MEDIUM",
            "rule_id": "PY100",
            "message": "疑似使用了未定义的名称 'Dot'（可能为动态导入或第三方库）。  （合并 2 条相似问题）",
            "snippet": "        arena.batch.add(Dot())",
            "count": 2,
            "examples": [
              13,
              28
            ]
          },
          {
            "file": "dot.py",
            "line": 25,
            "col": 11,
            "severity": "MEDIUM",
            "rule_id": "AST002",
            "message": "疑似使用 'is' 进行值比较，建议使用 '==' （is 仅用于 None/True/False）。  （合并 2 条相似问题）",
            "snippet": "        if color is None:",
            "count": 2,
            "examples": [
              25,
              31
            ]
          },
          {
            "file": "dot.py",
            "line": 64,
            "col": 8,
            "severity": "LOW",
            "rule_id": "PY011",
            "message": "过于宽泛的异常捕获：Exception。",
            "snippet": "        except Exception:",
            "count": 1,
            "examples": []
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 14,
              "row": 6
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import random\n\nfrom cocos.actions import CallFuncS, MoveTo\nfrom cocos.sprite import Sprite\n\nimport define\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 9
                  },
                  "location": {
                    "column": 1,
                    "row": 2
                  }
                }
              ],
              "message": "Organize imports"
            },
            "location": {
              "column": 1,
              "row": 2
            },
            "message": "Import block is un-sorted or un-formatted",
            "noqa_row": 2,
            "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E501",
            "end_location": {
              "column": 91,
              "row": 16
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "fix": null,
            "location": {
              "column": 89,
              "row": 16
            },
            "message": "Line too long (90 > 88)",
            "noqa_row": 16,
            "url": "https://docs.astral.sh/ruff/rules/line-too-long",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 25,
              "row": 65
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 25,
                    "row": 65
                  },
                  "location": {
                    "column": 25,
                    "row": 65
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 25,
              "row": 65
            },
            "message": "No newline at end of file",
            "noqa_row": 65,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "type": "error",
            "module": "dot",
            "obj": "",
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 43,
            "path": "dot.py",
            "symbol": "import-error",
            "message": "Unable to import 'cocos.actions'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "dot",
            "obj": "",
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 43,
            "path": "dot.py",
            "symbol": "no-name-in-module",
            "message": "No name 'actions' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "dot",
            "obj": "",
            "line": 4,
            "column": 0,
            "endLine": 4,
            "endColumn": 31,
            "path": "dot.py",
            "symbol": "import-error",
            "message": "Unable to import 'cocos.sprite'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "dot",
            "obj": "",
            "line": 4,
            "column": 0,
            "endLine": 4,
            "endColumn": 31,
            "path": "dot.py",
            "symbol": "no-name-in-module",
            "message": "No name 'sprite' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "dot",
            "obj": "Dot.update",
            "line": 42,
            "column": 21,
            "endLine": 42,
            "endColumn": 23,
            "path": "dot.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'dt'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "dot",
            "obj": "Dot.leak_file_handle",
            "line": 64,
            "column": 15,
            "endLine": 64,
            "endColumn": 24,
            "path": "dot.py",
            "symbol": "broad-exception-caught",
            "message": "Catching too general exception Exception",
            "message-id": "W0718",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "dot",
            "obj": "Dot.check_kill",
            "line": 54,
            "column": 12,
            "endLine": 54,
            "endColumn": 23,
            "path": "dot.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'killer' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "code": "25         if color is None:\n26             color = random.choice(define.ALL_COLOR)\n27 \n",
            "col_offset": 20,
            "end_col_offset": 51,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 26,
            "line_range": [
              26
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "31         if pos is None:\n32             self.position = (random.randint(40, define.WIDTH - 40),\n33                              random.randint(40, define.HEIGHT - 40))\n",
            "col_offset": 29,
            "end_col_offset": 66,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 32,
            "line_range": [
              32
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "32             self.position = (random.randint(40, define.WIDTH - 40),\n33                              random.randint(40, define.HEIGHT - 40))\n34             self.is_big = False\n",
            "col_offset": 29,
            "end_col_offset": 67,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 33,
            "line_range": [
              33
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "36         else:\n37             self.position = (pos[0] + random.random() * 32 - 16,\n38                              pos[1] + random.random() * 32 - 16)\n",
            "col_offset": 38,
            "end_col_offset": 53,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 37,
            "line_range": [
              37
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "37             self.position = (pos[0] + random.random() * 32 - 16,\n38                              pos[1] + random.random() * 32 - 16)\n39             self.is_big = True\n",
            "col_offset": 38,
            "end_col_offset": 53,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 38,
            "line_range": [
              38
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "39             self.is_big = True\n40         self.schedule_interval(self.update, random.random() * 0.2 + 0.1)\n41 \n",
            "col_offset": 44,
            "end_col_offset": 59,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 40,
            "line_range": [
              40
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          }
        ],
        "gameover.py": [
          {
            "file": "gameover.py",
            "line": 8,
            "col": 4,
            "severity": "HIGH",
            "rule_id": "AST001",
            "message": "函数 __init__ 的默认参数为可变对象，所有调用将共享同一对象。",
            "snippet": "    def __init__(self, banners=[]):",
            "count": 1,
            "examples": []
          },
          {
            "file": "gameover.py",
            "line": 11,
            "col": 8,
            "severity": "MEDIUM",
            "rule_id": "PY100",
            "message": "疑似使用了未定义的名称 'super'（可能为动态导入或第三方库）。",
            "snippet": "        super(Gameover, self).__init__(200, 235, 235, 200, 400, 300)",
            "count": 1,
            "examples": []
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 14,
              "row": 4
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gameover.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import cocos\nfrom cocos.director import director\n\nimport define\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 6
                  },
                  "location": {
                    "column": 1,
                    "row": 2
                  }
                }
              ],
              "message": "Organize imports"
            },
            "location": {
              "column": 1,
              "row": 2
            },
            "message": "Import block is un-sorted or un-formatted",
            "noqa_row": 2,
            "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "B006",
            "end_location": {
              "column": 34,
              "row": 8
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gameover.py",
            "fix": {
              "applicability": "unsafe",
              "edits": [
                {
                  "content": "None",
                  "end_location": {
                    "column": 34,
                    "row": 8
                  },
                  "location": {
                    "column": 32,
                    "row": 8
                  }
                },
                {
                  "content": "        if banners is None:\n            banners = []\n",
                  "end_location": {
                    "column": 1,
                    "row": 10
                  },
                  "location": {
                    "column": 1,
                    "row": 10
                  }
                }
              ],
              "message": "Replace with `None`; initialize within function"
            },
            "location": {
              "column": 32,
              "row": 8
            },
            "message": "Do not use mutable data structures for argument defaults",
            "noqa_row": 8,
            "url": "https://docs.astral.sh/ruff/rules/mutable-argument-default",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 23,
              "row": 34
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gameover.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 23,
                    "row": 34
                  },
                  "location": {
                    "column": 23,
                    "row": 34
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 23,
              "row": 34
            },
            "message": "No newline at end of file",
            "noqa_row": 34,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "type": "error",
            "module": "gameover",
            "obj": "",
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 35,
            "path": "gameover.py",
            "symbol": "import-error",
            "message": "Unable to import 'cocos.director'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gameover",
            "obj": "",
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 35,
            "path": "gameover.py",
            "symbol": "no-name-in-module",
            "message": "No name 'director' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gameover",
            "obj": "Gameover",
            "line": 6,
            "column": 15,
            "endLine": 6,
            "endColumn": 26,
            "path": "gameover.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'layer' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gameover",
            "obj": "Gameover.__init__",
            "line": 8,
            "column": 4,
            "endLine": 8,
            "endColumn": 16,
            "path": "gameover.py",
            "symbol": "dangerous-default-value",
            "message": "Dangerous default value [] as argument",
            "message-id": "W0102",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gameover",
            "obj": "Gameover.__init__",
            "line": 16,
            "column": 21,
            "endLine": 16,
            "endColumn": 31,
            "path": "gameover.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'text' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gameover",
            "obj": "Gameover.__init__",
            "line": 19,
            "column": 44,
            "endLine": 19,
            "endColumn": 58,
            "path": "gameover.py",
            "symbol": "no-member",
            "message": "Module 'define' has no 'MAROONS' member; maybe 'MAROON'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gameover",
            "obj": "Gameover.__init__",
            "line": 23,
            "column": 15,
            "endLine": 23,
            "endColumn": 25,
            "path": "gameover.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'text' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gameover",
            "obj": "Gameover.__init__",
            "line": 29,
            "column": 15,
            "endLine": 29,
            "endColumn": 25,
            "path": "gameover.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'text' member",
            "message-id": "E1101",
            "tool": "pylint"
          }
        ],
        "gluttonous.py": [
          {
            "file": "gluttonous.py",
            "line": 3,
            "col": 0,
            "severity": "MEDIUM",
            "rule_id": "PY100",
            "message": "疑似使用了未定义的名称 'cocos'（可能为动态导入或第三方库）。  （合并 3 条相似问题）",
            "snippet": "cocos.audio.initialize = lambda *args, **kwargs: None  # 空函数",
            "count": 3,
            "examples": [
              3,
              36,
              69
            ]
          },
          {
            "file": "gluttonous.py",
            "line": 19,
            "col": 19,
            "severity": "HIGH",
            "rule_id": "PY001",
            "message": "使用 eval 可能导致代码执行漏洞。",
            "snippet": "            return eval(expr)",
            "count": 1,
            "examples": []
          },
          {
            "file": "gluttonous.py",
            "line": 20,
            "col": 4,
            "severity": "LOW",
            "rule_id": "PY011",
            "message": "过于宽泛的异常捕获：Exception。  （合并 2 条相似问题）",
            "snippet": "    except Exception:",
            "count": 2,
            "examples": [
              20,
              29
            ]
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 19,
              "row": 2
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import cocos.audio\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 3
                  },
                  "location": {
                    "column": 1,
                    "row": 2
                  }
                }
              ],
              "message": "Organize imports"
            },
            "location": {
              "column": 1,
              "row": 2
            },
            "message": "Import block is un-sorted or un-formatted",
            "noqa_row": 2,
            "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E402",
            "end_location": {
              "column": 13,
              "row": 6
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": null,
            "location": {
              "column": 1,
              "row": 6
            },
            "message": "Module level import not at top of file",
            "noqa_row": 6,
            "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 30,
              "row": 12
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import cocos\nfrom cocos.director import director\nfrom cocos.scene import Scene\n\nimport define\nfrom arena import Arena\nfrom gameover import Gameover\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 14
                  },
                  "location": {
                    "column": 1,
                    "row": 6
                  }
                }
              ],
              "message": "Organize imports"
            },
            "location": {
              "column": 1,
              "row": 6
            },
            "message": "Import block is un-sorted or un-formatted",
            "noqa_row": 6,
            "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E402",
            "end_location": {
              "column": 36,
              "row": 7
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": null,
            "location": {
              "column": 1,
              "row": 7
            },
            "message": "Module level import not at top of file",
            "noqa_row": 7,
            "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E402",
            "end_location": {
              "column": 30,
              "row": 8
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": null,
            "location": {
              "column": 1,
              "row": 8
            },
            "message": "Module level import not at top of file",
            "noqa_row": 8,
            "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E402",
            "end_location": {
              "column": 14,
              "row": 10
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": null,
            "location": {
              "column": 1,
              "row": 10
            },
            "message": "Module level import not at top of file",
            "noqa_row": 10,
            "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E402",
            "end_location": {
              "column": 24,
              "row": 11
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": null,
            "location": {
              "column": 1,
              "row": 11
            },
            "message": "Module level import not at top of file",
            "noqa_row": 11,
            "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E402",
            "end_location": {
              "column": 30,
              "row": 12
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": null,
            "location": {
              "column": 1,
              "row": 12
            },
            "message": "Module level import not at top of file",
            "noqa_row": 12,
            "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "F821",
            "end_location": {
              "column": 30,
              "row": 69
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": null,
            "location": {
              "column": 20,
              "row": 69
            },
            "message": "Undefined name `HelloWrold`",
            "noqa_row": 69,
            "url": "https://docs.astral.sh/ruff/rules/undefined-name",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 34,
              "row": 69
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 34,
                    "row": 69
                  },
                  "location": {
                    "column": 34,
                    "row": 69
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 34,
              "row": 69
            },
            "message": "No newline at end of file",
            "noqa_row": 69,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 2,
            "column": 0,
            "endLine": 2,
            "endColumn": 18,
            "path": "gluttonous.py",
            "symbol": "import-error",
            "message": "Unable to import 'cocos.audio'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 2,
            "column": 0,
            "endLine": 2,
            "endColumn": 18,
            "path": "gluttonous.py",
            "symbol": "no-name-in-module",
            "message": "No name 'audio' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 11,
            "path": "gluttonous.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'audio' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 7,
            "column": 0,
            "endLine": 7,
            "endColumn": 35,
            "path": "gluttonous.py",
            "symbol": "import-error",
            "message": "Unable to import 'cocos.director'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 7,
            "column": 0,
            "endLine": 7,
            "endColumn": 35,
            "path": "gluttonous.py",
            "symbol": "no-name-in-module",
            "message": "No name 'director' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 8,
            "column": 0,
            "endLine": 8,
            "endColumn": 29,
            "path": "gluttonous.py",
            "symbol": "import-error",
            "message": "Unable to import 'cocos.scene'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 8,
            "column": 0,
            "endLine": 8,
            "endColumn": 29,
            "path": "gluttonous.py",
            "symbol": "no-name-in-module",
            "message": "No name 'scene' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "unsafe_eval",
            "line": 20,
            "column": 11,
            "endLine": 20,
            "endColumn": 20,
            "path": "gluttonous.py",
            "symbol": "broad-exception-caught",
            "message": "Catching too general exception Exception",
            "message-id": "W0718",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "unsafe_eval",
            "line": 19,
            "column": 19,
            "endLine": 19,
            "endColumn": 29,
            "path": "gluttonous.py",
            "symbol": "eval-used",
            "message": "Use of eval",
            "message-id": "W0123",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "leak_file_helper",
            "line": 29,
            "column": 11,
            "endLine": 29,
            "endColumn": 20,
            "path": "gluttonous.py",
            "symbol": "broad-exception-caught",
            "message": "Catching too general exception Exception",
            "message-id": "W0718",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "HelloWorld",
            "line": 32,
            "column": 17,
            "endLine": 32,
            "endColumn": 28,
            "path": "gluttonous.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'layer' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "HelloWorld.__init__",
            "line": 40,
            "column": 21,
            "endLine": 40,
            "endColumn": 31,
            "path": "gluttonous.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'text' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "HelloWorld.on_mouse_press",
            "line": 57,
            "column": 29,
            "endLine": 57,
            "endColumn": 30,
            "path": "gluttonous.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'x'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "HelloWorld.on_mouse_press",
            "line": 57,
            "column": 32,
            "endLine": 57,
            "endColumn": 33,
            "path": "gluttonous.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'y'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "HelloWorld.on_mouse_press",
            "line": 57,
            "column": 35,
            "endLine": 57,
            "endColumn": 42,
            "path": "gluttonous.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'buttons'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "HelloWorld.on_mouse_press",
            "line": 57,
            "column": 44,
            "endLine": 57,
            "endColumn": 53,
            "path": "gluttonous.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'modifiers'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 69,
            "column": 19,
            "endLine": 69,
            "endColumn": 29,
            "path": "gluttonous.py",
            "symbol": "undefined-variable",
            "message": "Undefined variable 'HelloWrold'",
            "message-id": "E0602",
            "tool": "pylint"
          },
          {
            "code": "18         if isinstance(expr, str) and len(expr) < 50:\n19             return eval(expr)\n20     except Exception:\n",
            "col_offset": 19,
            "end_col_offset": 29,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 78,
              "link": "https://cwe.mitre.org/data/definitions/78.html"
            },
            "issue_severity": "MEDIUM",
            "issue_text": "Use of possibly insecure function - consider using safer ast.literal_eval.",
            "line_number": 19,
            "line_range": [
              19
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b307-eval",
            "test_id": "B307",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "28         # intentionally not closing here for detection exercises\n29     except Exception:\n30         pass\n31 \n",
            "col_offset": 4,
            "end_col_offset": 12,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 703,
              "link": "https://cwe.mitre.org/data/definitions/703.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Try, Except, Pass detected.",
            "line_number": 29,
            "line_range": [
              29,
              30
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b110_try_except_pass.html",
            "test_id": "B110",
            "test_name": "try_except_pass",
            "tool": "bandit"
          }
        ],
        "snake.py": [
          {
            "file": "snake.py",
            "line": 16,
            "col": 8,
            "severity": "MEDIUM",
            "rule_id": "PY100",
            "message": "疑似使用了未定义的名称 'super'（可能为动态导入或第三方库）。  （合并 2 条相似问题）",
            "snippet": "        super(Snake, self).__init__()",
            "count": 2,
            "examples": [
              16,
              117
            ]
          },
          {
            "file": "snake.py",
            "line": 68,
            "col": 8,
            "severity": "LOW",
            "rule_id": "PY010",
            "message": "使用裸 except，建议捕获具体异常类型。",
            "snippet": "        except:",
            "count": 1,
            "examples": []
          },
          {
            "file": "snake.py",
            "line": 81,
            "col": 8,
            "severity": "HIGH",
            "rule_id": "PY003",
            "message": "subprocess.*(shell=True) 可能导致命令注入。",
            "snippet": "        subprocess.run(\"echo harmless\", shell=True)",
            "count": 1,
            "examples": []
          },
          {
            "file": "snake.py",
            "line": 139,
            "col": 11,
            "severity": "MEDIUM",
            "rule_id": "AST002",
            "message": "疑似使用 'is' 进行值比较，建议使用 '==' （is 仅用于 None/True/False）。",
            "snippet": "        if direct is None:",
            "count": 1,
            "examples": []
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 20,
              "row": 9
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import math\nimport random\nimport sys  # Intentional: unused import to be flagged by linters\n\nimport cocos\nfrom cocos.sprite import Sprite\n\nimport define\nfrom dot import Dot\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 12
                  },
                  "location": {
                    "column": 1,
                    "row": 2
                  }
                }
              ],
              "message": "Organize imports"
            },
            "location": {
              "column": 1,
              "row": 2
            },
            "message": "Import block is un-sorted or un-formatted",
            "noqa_row": 2,
            "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "F401",
            "end_location": {
              "column": 11,
              "row": 3
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "",
                  "end_location": {
                    "column": 1,
                    "row": 4
                  },
                  "location": {
                    "column": 1,
                    "row": 3
                  }
                }
              ],
              "message": "Remove unused import: `sys`"
            },
            "location": {
              "column": 8,
              "row": 3
            },
            "message": "`sys` imported but unused",
            "noqa_row": 3,
            "url": "https://docs.astral.sh/ruff/rules/unused-import",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E722",
            "end_location": {
              "column": 15,
              "row": 68
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "fix": null,
            "location": {
              "column": 9,
              "row": 68
            },
            "message": "Do not use bare `except`",
            "noqa_row": 68,
            "url": "https://docs.astral.sh/ruff/rules/bare-except",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "B007",
            "end_location": {
              "column": 14,
              "row": 87
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "fix": {
              "applicability": "unsafe",
              "edits": [
                {
                  "content": "_i",
                  "end_location": {
                    "column": 14,
                    "row": 87
                  },
                  "location": {
                    "column": 13,
                    "row": 87
                  }
                }
              ],
              "message": "Rename unused `i` to `_i`"
            },
            "location": {
              "column": 13,
              "row": 87
            },
            "message": "Loop control variable `i` not used within loop body",
            "noqa_row": 87,
            "url": "https://docs.astral.sh/ruff/rules/unused-loop-control-variable",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E741",
            "end_location": {
              "column": 10,
              "row": 148
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "fix": null,
            "location": {
              "column": 9,
              "row": 148
            },
            "message": "Ambiguous variable name: `l`",
            "noqa_row": 148,
            "url": "https://docs.astral.sh/ruff/rules/ambiguous-variable-name",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 40,
              "row": 225
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 40,
                    "row": 225
                  },
                  "location": {
                    "column": 40,
                    "row": 225
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 40,
              "row": 225
            },
            "message": "No newline at end of file",
            "noqa_row": 225,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "",
            "line": 6,
            "column": 0,
            "endLine": 6,
            "endColumn": 31,
            "path": "snake.py",
            "symbol": "import-error",
            "message": "Unable to import 'cocos.sprite'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "",
            "line": 6,
            "column": 0,
            "endLine": 6,
            "endColumn": 31,
            "path": "snake.py",
            "symbol": "no-name-in-module",
            "message": "No name 'sprite' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake",
            "line": 12,
            "column": 12,
            "endLine": 12,
            "endColumn": 27,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'cocosnode' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.__init__",
            "line": 25,
            "column": 21,
            "endLine": 25,
            "endColumn": 27,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.__init__",
            "line": 26,
            "column": 16,
            "endLine": 26,
            "endColumn": 22,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.add_body",
            "line": 63,
            "column": 11,
            "endLine": 63,
            "endColumn": 17,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.add_body",
            "line": 68,
            "column": 8,
            "endLine": 69,
            "endColumn": 53,
            "path": "snake.py",
            "symbol": "bare-except",
            "message": "No exception type(s) specified",
            "message-id": "W0702",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.maybe_shell_call",
            "line": 81,
            "column": 8,
            "endLine": 81,
            "endColumn": 51,
            "path": "snake.py",
            "symbol": "subprocess-run-check",
            "message": "'subprocess.run' used without explicitly defining the value for 'check'.",
            "message-id": "W1510",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.init_body",
            "line": 87,
            "column": 12,
            "endLine": 87,
            "endColumn": 13,
            "path": "snake.py",
            "symbol": "unused-variable",
            "message": "Unused variable 'i'",
            "message-id": "W0612",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.update",
            "line": 112,
            "column": 8,
            "endLine": 112,
            "endColumn": 14,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.update",
            "line": 113,
            "column": 8,
            "endLine": 113,
            "endColumn": 14,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.ai",
            "line": 155,
            "column": 12,
            "endLine": 155,
            "endColumn": 18,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.ai",
            "line": 156,
            "column": 12,
            "endLine": 156,
            "endColumn": 18,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.ai",
            "line": 160,
            "column": 14,
            "endLine": 160,
            "endColumn": 20,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.ai",
            "line": 161,
            "column": 12,
            "endLine": 161,
            "endColumn": 18,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.ai",
            "line": 153,
            "column": 17,
            "endLine": 153,
            "endColumn": 19,
            "path": "snake.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'dt'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.collision_detect",
            "line": 175,
            "column": 24,
            "endLine": 175,
            "endColumn": 30,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.collision_detect",
            "line": 176,
            "column": 24,
            "endLine": 176,
            "endColumn": 30,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.check_crash",
            "line": 195,
            "column": 12,
            "endLine": 195,
            "endColumn": 18,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.check_crash",
            "line": 195,
            "column": 26,
            "endLine": 195,
            "endColumn": 32,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.check_crash",
            "line": 196,
            "column": 12,
            "endLine": 196,
            "endColumn": 18,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.check_crash",
            "line": 196,
            "column": 26,
            "endLine": 196,
            "endColumn": 32,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.check_crash",
            "line": 201,
            "column": 35,
            "endLine": 201,
            "endColumn": 41,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.check_crash",
            "line": 201,
            "column": 57,
            "endLine": 201,
            "endColumn": 63,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.init_body",
            "line": 84,
            "column": 8,
            "endLine": 84,
            "endColumn": 18,
            "path": "snake.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'score' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.init_body",
            "line": 85,
            "column": 8,
            "endLine": 85,
            "endColumn": 19,
            "path": "snake.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'length' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.add_score",
            "line": 150,
            "column": 12,
            "endLine": 150,
            "endColumn": 23,
            "path": "snake.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'length' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.init_body",
            "line": 86,
            "column": 8,
            "endLine": 86,
            "endColumn": 17,
            "path": "snake.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'body' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "",
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 10,
            "path": "snake.py",
            "symbol": "unused-import",
            "message": "Unused import sys",
            "message-id": "W0611",
            "tool": "pylint"
          },
          {
            "code": "17         self.is_dead = False\n18         self.angle = random.randrange(360)  # 目前角度\n19         self.angle_dest = self.angle  # 目标角度\n",
            "col_offset": 21,
            "end_col_offset": 42,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 18,
            "line_range": [
              18
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "19         self.angle_dest = self.angle  # 目标角度\n20         self.color = random.choice(define.ALL_COLOR)\n21         self.no = Snake.no\n",
            "col_offset": 21,
            "end_col_offset": 52,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 20,
            "line_range": [
              20
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "23         if is_enemy:\n24             self.position = random.randrange(300, 1300), random.randrange(200, 600)\n25             if 600 < self.x < 1000:\n",
            "col_offset": 28,
            "end_col_offset": 55,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 24,
            "line_range": [
              24
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "23         if is_enemy:\n24             self.position = random.randrange(300, 1300), random.randrange(200, 600)\n25             if 600 < self.x < 1000:\n",
            "col_offset": 57,
            "end_col_offset": 83,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 24,
            "line_range": [
              24
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "27         else:\n28             self.position = random.randrange(700, 900), random.randrange(350, 450)\n29         self.is_enemy = is_enemy\n",
            "col_offset": 28,
            "end_col_offset": 54,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 28,
            "line_range": [
              28
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "27         else:\n28             self.position = random.randrange(700, 900), random.randrange(350, 450)\n29         self.is_enemy = is_enemy\n",
            "col_offset": 56,
            "end_col_offset": 82,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 28,
            "line_range": [
              28
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "56         if self.is_enemy:\n57             self.schedule_interval(self.ai, random.random() * 0.1 + 0.05)\n58 \n",
            "col_offset": 44,
            "end_col_offset": 59,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 57,
            "line_range": [
              57
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "78         Not called by default; present for dynamic detection exercises.\"\"\"\n79         import subprocess\n80         # benign command; uses shell=True to be flagged by scanners\n",
            "col_offset": 8,
            "end_col_offset": 25,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 78,
              "link": "https://cwe.mitre.org/data/definitions/78.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Consider possible security implications associated with the subprocess module.",
            "line_number": 79,
            "line_range": [
              79
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_imports.html#b404-import-subprocess",
            "test_id": "B404",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "80         # benign command; uses shell=True to be flagged by scanners\n81         subprocess.run(\"echo harmless\", shell=True)\n82 \n",
            "col_offset": 8,
            "end_col_offset": 51,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 78,
              "link": "https://cwe.mitre.org/data/definitions/78.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Starting a process with a partial executable path",
            "line_number": 81,
            "line_range": [
              81
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b607_start_process_with_partial_path.html",
            "test_id": "B607",
            "test_name": "start_process_with_partial_path",
            "tool": "bandit"
          },
          {
            "code": "80         # benign command; uses shell=True to be flagged by scanners\n81         subprocess.run(\"echo harmless\", shell=True)\n82 \n",
            "col_offset": 8,
            "end_col_offset": 51,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 78,
              "link": "https://cwe.mitre.org/data/definitions/78.html"
            },
            "issue_severity": "LOW",
            "issue_text": "subprocess call with shell=True seems safe, but may be changed in the future, consider rewriting without shell",
            "line_number": 81,
            "line_range": [
              81
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b602_subprocess_popen_with_shell_equals_true.html",
            "test_id": "B602",
            "test_name": "subprocess_popen_with_shell_equals_true",
            "tool": "bandit"
          },
          {
            "code": "189             if abs(angle - self.angle_dest) < 5:\n190                 self.angle_dest += random.randrange(90, 270)\n191 \n",
            "col_offset": 35,
            "end_col_offset": 60,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 190,
            "line_range": [
              190
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          }
        ],
        "define.py": [
          {
            "cell": null,
            "code": "F401",
            "end_location": {
              "column": 14,
              "row": 2
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\define.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "",
                  "end_location": {
                    "column": 1,
                    "row": 3
                  },
                  "location": {
                    "column": 1,
                    "row": 2
                  }
                }
              ],
              "message": "Remove unused import: `random`"
            },
            "location": {
              "column": 8,
              "row": 2
            },
            "message": "`random` imported but unused",
            "noqa_row": 2,
            "url": "https://docs.astral.sh/ruff/rules/unused-import",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 15,
              "row": 29
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\define.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 15,
                    "row": 29
                  },
                  "location": {
                    "column": 15,
                    "row": 29
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 15,
              "row": 29
            },
            "message": "No newline at end of file",
            "noqa_row": 29,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "type": "warning",
            "module": "define",
            "obj": "",
            "line": 2,
            "column": 0,
            "endLine": 2,
            "endColumn": 13,
            "path": "define.py",
            "symbol": "unused-import",
            "message": "Unused import random",
            "message-id": "W0611",
            "tool": "pylint"
          }
        ]
      },
      "issues_by_severity": {
        "HIGH": [
          {
            "file": "gameover.py",
            "line": 8,
            "col": 4,
            "severity": "HIGH",
            "rule_id": "AST001",
            "message": "函数 __init__ 的默认参数为可变对象，所有调用将共享同一对象。",
            "snippet": "    def __init__(self, banners=[]):",
            "count": 1,
            "examples": []
          },
          {
            "file": "gluttonous.py",
            "line": 19,
            "col": 19,
            "severity": "HIGH",
            "rule_id": "PY001",
            "message": "使用 eval 可能导致代码执行漏洞。",
            "snippet": "            return eval(expr)",
            "count": 1,
            "examples": []
          },
          {
            "file": "snake.py",
            "line": 81,
            "col": 8,
            "severity": "HIGH",
            "rule_id": "PY003",
            "message": "subprocess.*(shell=True) 可能导致命令注入。",
            "snippet": "        subprocess.run(\"echo harmless\", shell=True)",
            "count": 1,
            "examples": []
          }
        ],
        "MEDIUM": [
          {
            "file": "arena.py",
            "line": 12,
            "col": 8,
            "severity": "MEDIUM",
            "rule_id": "PY100",
            "message": "疑似使用了未定义的名称 'super'（可能为动态导入或第三方库）。",
            "snippet": "        super(Arena, self).__init__(250, 255, 255, 255, define.WIDTH, define.HEIGHT)",
            "count": 1,
            "examples": []
          },
          {
            "file": "dot.py",
            "line": 13,
            "col": 24,
            "severity": "MEDIUM",
            "rule_id": "PY100",
            "message": "疑似使用了未定义的名称 'Dot'（可能为动态导入或第三方库）。  （合并 2 条相似问题）",
            "snippet": "        arena.batch.add(Dot())",
            "count": 2,
            "examples": [
              13,
              28
            ]
          },
          {
            "file": "dot.py",
            "line": 25,
            "col": 11,
            "severity": "MEDIUM",
            "rule_id": "AST002",
            "message": "疑似使用 'is' 进行值比较，建议使用 '==' （is 仅用于 None/True/False）。  （合并 2 条相似问题）",
            "snippet": "        if color is None:",
            "count": 2,
            "examples": [
              25,
              31
            ]
          },
          {
            "file": "gameover.py",
            "line": 11,
            "col": 8,
            "severity": "MEDIUM",
            "rule_id": "PY100",
            "message": "疑似使用了未定义的名称 'super'（可能为动态导入或第三方库）。",
            "snippet": "        super(Gameover, self).__init__(200, 235, 235, 200, 400, 300)",
            "count": 1,
            "examples": []
          },
          {
            "file": "gluttonous.py",
            "line": 3,
            "col": 0,
            "severity": "MEDIUM",
            "rule_id": "PY100",
            "message": "疑似使用了未定义的名称 'cocos'（可能为动态导入或第三方库）。  （合并 3 条相似问题）",
            "snippet": "cocos.audio.initialize = lambda *args, **kwargs: None  # 空函数",
            "count": 3,
            "examples": [
              3,
              36,
              69
            ]
          },
          {
            "file": "snake.py",
            "line": 16,
            "col": 8,
            "severity": "MEDIUM",
            "rule_id": "PY100",
            "message": "疑似使用了未定义的名称 'super'（可能为动态导入或第三方库）。  （合并 2 条相似问题）",
            "snippet": "        super(Snake, self).__init__()",
            "count": 2,
            "examples": [
              16,
              117
            ]
          },
          {
            "file": "snake.py",
            "line": 139,
            "col": 11,
            "severity": "MEDIUM",
            "rule_id": "AST002",
            "message": "疑似使用 'is' 进行值比较，建议使用 '==' （is 仅用于 None/True/False）。",
            "snippet": "        if direct is None:",
            "count": 1,
            "examples": []
          }
        ],
        "LOW": [
          {
            "file": "arena.py",
            "line": 42,
            "col": 8,
            "severity": "LOW",
            "rule_id": "PY010",
            "message": "使用裸 except，建议捕获具体异常类型。",
            "snippet": "        except:",
            "count": 1,
            "examples": []
          },
          {
            "file": "dot.py",
            "line": 64,
            "col": 8,
            "severity": "LOW",
            "rule_id": "PY011",
            "message": "过于宽泛的异常捕获：Exception。",
            "snippet": "        except Exception:",
            "count": 1,
            "examples": []
          },
          {
            "file": "gluttonous.py",
            "line": 20,
            "col": 4,
            "severity": "LOW",
            "rule_id": "PY011",
            "message": "过于宽泛的异常捕获：Exception。  （合并 2 条相似问题）",
            "snippet": "    except Exception:",
            "count": 2,
            "examples": [
              20,
              29
            ]
          },
          {
            "file": "snake.py",
            "line": 68,
            "col": 8,
            "severity": "LOW",
            "rule_id": "PY010",
            "message": "使用裸 except，建议捕获具体异常类型。",
            "snippet": "        except:",
            "count": 1,
            "examples": []
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 20,
              "row": 6
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import cocos\nfrom cocos.director import director\n\nimport define\nfrom dot import Dot\nfrom snake import (\n    Snake,  # keep original import; note: mismatch with snake_game.py if that's the actual file\n)\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 8
                  },
                  "location": {
                    "column": 1,
                    "row": 1
                  }
                }
              ],
              "message": "Organize imports"
            },
            "location": {
              "column": 1,
              "row": 1
            },
            "message": "Import block is un-sorted or un-formatted",
            "noqa_row": 1,
            "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E501",
            "end_location": {
              "column": 109,
              "row": 5
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
            "fix": null,
            "location": {
              "column": 89,
              "row": 5
            },
            "message": "Line too long (108 > 88)",
            "noqa_row": 5,
            "url": "https://docs.astral.sh/ruff/rules/line-too-long",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E501",
            "end_location": {
              "column": 93,
              "row": 13
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
            "fix": null,
            "location": {
              "column": 89,
              "row": 13
            },
            "message": "Line too long (92 > 88)",
            "noqa_row": 13,
            "url": "https://docs.astral.sh/ruff/rules/line-too-long",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "B007",
            "end_location": {
              "column": 14,
              "row": 22
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
            "fix": {
              "applicability": "unsafe",
              "edits": [
                {
                  "content": "_i",
                  "end_location": {
                    "column": 14,
                    "row": 22
                  },
                  "location": {
                    "column": 13,
                    "row": 22
                  }
                }
              ],
              "message": "Rename unused `i` to `_i`"
            },
            "location": {
              "column": 13,
              "row": 22
            },
            "message": "Loop control variable `i` not used within loop body",
            "noqa_row": 22,
            "url": "https://docs.astral.sh/ruff/rules/unused-loop-control-variable",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "B007",
            "end_location": {
              "column": 14,
              "row": 27
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
            "fix": {
              "applicability": "unsafe",
              "edits": [
                {
                  "content": "_i",
                  "end_location": {
                    "column": 14,
                    "row": 27
                  },
                  "location": {
                    "column": 13,
                    "row": 27
                  }
                }
              ],
              "message": "Rename unused `i` to `_i`"
            },
            "location": {
              "column": 13,
              "row": 27
            },
            "message": "Loop control variable `i` not used within loop body",
            "noqa_row": 27,
            "url": "https://docs.astral.sh/ruff/rules/unused-loop-control-variable",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E722",
            "end_location": {
              "column": 15,
              "row": 42
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
            "fix": null,
            "location": {
              "column": 9,
              "row": 42
            },
            "message": "Do not use bare `except`",
            "noqa_row": 42,
            "url": "https://docs.astral.sh/ruff/rules/bare-except",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 51,
              "row": 59
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 51,
                    "row": 59
                  },
                  "location": {
                    "column": 51,
                    "row": 59
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 51,
              "row": 59
            },
            "message": "No newline at end of file",
            "noqa_row": 59,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "F401",
            "end_location": {
              "column": 14,
              "row": 2
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\define.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "",
                  "end_location": {
                    "column": 1,
                    "row": 3
                  },
                  "location": {
                    "column": 1,
                    "row": 2
                  }
                }
              ],
              "message": "Remove unused import: `random`"
            },
            "location": {
              "column": 8,
              "row": 2
            },
            "message": "`random` imported but unused",
            "noqa_row": 2,
            "url": "https://docs.astral.sh/ruff/rules/unused-import",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 15,
              "row": 29
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\define.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 15,
                    "row": 29
                  },
                  "location": {
                    "column": 15,
                    "row": 29
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 15,
              "row": 29
            },
            "message": "No newline at end of file",
            "noqa_row": 29,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 14,
              "row": 6
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import random\n\nfrom cocos.actions import CallFuncS, MoveTo\nfrom cocos.sprite import Sprite\n\nimport define\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 9
                  },
                  "location": {
                    "column": 1,
                    "row": 2
                  }
                }
              ],
              "message": "Organize imports"
            },
            "location": {
              "column": 1,
              "row": 2
            },
            "message": "Import block is un-sorted or un-formatted",
            "noqa_row": 2,
            "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E501",
            "end_location": {
              "column": 91,
              "row": 16
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "fix": null,
            "location": {
              "column": 89,
              "row": 16
            },
            "message": "Line too long (90 > 88)",
            "noqa_row": 16,
            "url": "https://docs.astral.sh/ruff/rules/line-too-long",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 25,
              "row": 65
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 25,
                    "row": 65
                  },
                  "location": {
                    "column": 25,
                    "row": 65
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 25,
              "row": 65
            },
            "message": "No newline at end of file",
            "noqa_row": 65,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 14,
              "row": 4
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gameover.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import cocos\nfrom cocos.director import director\n\nimport define\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 6
                  },
                  "location": {
                    "column": 1,
                    "row": 2
                  }
                }
              ],
              "message": "Organize imports"
            },
            "location": {
              "column": 1,
              "row": 2
            },
            "message": "Import block is un-sorted or un-formatted",
            "noqa_row": 2,
            "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "B006",
            "end_location": {
              "column": 34,
              "row": 8
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gameover.py",
            "fix": {
              "applicability": "unsafe",
              "edits": [
                {
                  "content": "None",
                  "end_location": {
                    "column": 34,
                    "row": 8
                  },
                  "location": {
                    "column": 32,
                    "row": 8
                  }
                },
                {
                  "content": "        if banners is None:\n            banners = []\n",
                  "end_location": {
                    "column": 1,
                    "row": 10
                  },
                  "location": {
                    "column": 1,
                    "row": 10
                  }
                }
              ],
              "message": "Replace with `None`; initialize within function"
            },
            "location": {
              "column": 32,
              "row": 8
            },
            "message": "Do not use mutable data structures for argument defaults",
            "noqa_row": 8,
            "url": "https://docs.astral.sh/ruff/rules/mutable-argument-default",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 23,
              "row": 34
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gameover.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 23,
                    "row": 34
                  },
                  "location": {
                    "column": 23,
                    "row": 34
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 23,
              "row": 34
            },
            "message": "No newline at end of file",
            "noqa_row": 34,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 19,
              "row": 2
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import cocos.audio\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 3
                  },
                  "location": {
                    "column": 1,
                    "row": 2
                  }
                }
              ],
              "message": "Organize imports"
            },
            "location": {
              "column": 1,
              "row": 2
            },
            "message": "Import block is un-sorted or un-formatted",
            "noqa_row": 2,
            "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E402",
            "end_location": {
              "column": 13,
              "row": 6
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": null,
            "location": {
              "column": 1,
              "row": 6
            },
            "message": "Module level import not at top of file",
            "noqa_row": 6,
            "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 30,
              "row": 12
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import cocos\nfrom cocos.director import director\nfrom cocos.scene import Scene\n\nimport define\nfrom arena import Arena\nfrom gameover import Gameover\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 14
                  },
                  "location": {
                    "column": 1,
                    "row": 6
                  }
                }
              ],
              "message": "Organize imports"
            },
            "location": {
              "column": 1,
              "row": 6
            },
            "message": "Import block is un-sorted or un-formatted",
            "noqa_row": 6,
            "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E402",
            "end_location": {
              "column": 36,
              "row": 7
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": null,
            "location": {
              "column": 1,
              "row": 7
            },
            "message": "Module level import not at top of file",
            "noqa_row": 7,
            "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E402",
            "end_location": {
              "column": 30,
              "row": 8
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": null,
            "location": {
              "column": 1,
              "row": 8
            },
            "message": "Module level import not at top of file",
            "noqa_row": 8,
            "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E402",
            "end_location": {
              "column": 14,
              "row": 10
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": null,
            "location": {
              "column": 1,
              "row": 10
            },
            "message": "Module level import not at top of file",
            "noqa_row": 10,
            "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E402",
            "end_location": {
              "column": 24,
              "row": 11
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": null,
            "location": {
              "column": 1,
              "row": 11
            },
            "message": "Module level import not at top of file",
            "noqa_row": 11,
            "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E402",
            "end_location": {
              "column": 30,
              "row": 12
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": null,
            "location": {
              "column": 1,
              "row": 12
            },
            "message": "Module level import not at top of file",
            "noqa_row": 12,
            "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "F821",
            "end_location": {
              "column": 30,
              "row": 69
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": null,
            "location": {
              "column": 20,
              "row": 69
            },
            "message": "Undefined name `HelloWrold`",
            "noqa_row": 69,
            "url": "https://docs.astral.sh/ruff/rules/undefined-name",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 34,
              "row": 69
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 34,
                    "row": 69
                  },
                  "location": {
                    "column": 34,
                    "row": 69
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 34,
              "row": 69
            },
            "message": "No newline at end of file",
            "noqa_row": 69,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 20,
              "row": 9
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import math\nimport random\nimport sys  # Intentional: unused import to be flagged by linters\n\nimport cocos\nfrom cocos.sprite import Sprite\n\nimport define\nfrom dot import Dot\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 12
                  },
                  "location": {
                    "column": 1,
                    "row": 2
                  }
                }
              ],
              "message": "Organize imports"
            },
            "location": {
              "column": 1,
              "row": 2
            },
            "message": "Import block is un-sorted or un-formatted",
            "noqa_row": 2,
            "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "F401",
            "end_location": {
              "column": 11,
              "row": 3
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "",
                  "end_location": {
                    "column": 1,
                    "row": 4
                  },
                  "location": {
                    "column": 1,
                    "row": 3
                  }
                }
              ],
              "message": "Remove unused import: `sys`"
            },
            "location": {
              "column": 8,
              "row": 3
            },
            "message": "`sys` imported but unused",
            "noqa_row": 3,
            "url": "https://docs.astral.sh/ruff/rules/unused-import",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E722",
            "end_location": {
              "column": 15,
              "row": 68
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "fix": null,
            "location": {
              "column": 9,
              "row": 68
            },
            "message": "Do not use bare `except`",
            "noqa_row": 68,
            "url": "https://docs.astral.sh/ruff/rules/bare-except",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "B007",
            "end_location": {
              "column": 14,
              "row": 87
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "fix": {
              "applicability": "unsafe",
              "edits": [
                {
                  "content": "_i",
                  "end_location": {
                    "column": 14,
                    "row": 87
                  },
                  "location": {
                    "column": 13,
                    "row": 87
                  }
                }
              ],
              "message": "Rename unused `i` to `_i`"
            },
            "location": {
              "column": 13,
              "row": 87
            },
            "message": "Loop control variable `i` not used within loop body",
            "noqa_row": 87,
            "url": "https://docs.astral.sh/ruff/rules/unused-loop-control-variable",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E741",
            "end_location": {
              "column": 10,
              "row": 148
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "fix": null,
            "location": {
              "column": 9,
              "row": 148
            },
            "message": "Ambiguous variable name: `l`",
            "noqa_row": 148,
            "url": "https://docs.astral.sh/ruff/rules/ambiguous-variable-name",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 40,
              "row": 225
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 40,
                    "row": 225
                  },
                  "location": {
                    "column": 40,
                    "row": 225
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 40,
              "row": 225
            },
            "message": "No newline at end of file",
            "noqa_row": 225,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "",
            "line": 2,
            "column": 0,
            "endLine": 2,
            "endColumn": 35,
            "path": "arena.py",
            "symbol": "import-error",
            "message": "Unable to import 'cocos.director'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "",
            "line": 2,
            "column": 0,
            "endLine": 2,
            "endColumn": 35,
            "path": "arena.py",
            "symbol": "no-name-in-module",
            "message": "No name 'director' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "Arena",
            "line": 8,
            "column": 12,
            "endLine": 8,
            "endColumn": 23,
            "path": "arena.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'layer' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "Arena.__init__",
            "line": 14,
            "column": 21,
            "endLine": 14,
            "endColumn": 32,
            "path": "arena.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'batch' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.__init__",
            "line": 22,
            "column": 12,
            "endLine": 22,
            "endColumn": 13,
            "path": "arena.py",
            "symbol": "unused-variable",
            "message": "Unused variable 'i'",
            "message-id": "W0612",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.add_enemy",
            "line": 42,
            "column": 8,
            "endLine": 44,
            "endColumn": 16,
            "path": "arena.py",
            "symbol": "bare-except",
            "message": "No exception type(s) specified",
            "message-id": "W0702",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "Arena.update",
            "line": 47,
            "column": 34,
            "endLine": 47,
            "endColumn": 46,
            "path": "arena.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "Arena.update",
            "line": 48,
            "column": 34,
            "endLine": 48,
            "endColumn": 46,
            "path": "arena.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "Arena.update",
            "line": 50,
            "column": 8,
            "endLine": 50,
            "endColumn": 22,
            "path": "arena.py",
            "symbol": "no-member",
            "message": "Instance of 'Arena' has no 'undefined' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.update",
            "line": 46,
            "column": 21,
            "endLine": 46,
            "endColumn": 23,
            "path": "arena.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'dt'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.on_key_press",
            "line": 52,
            "column": 32,
            "endLine": 52,
            "endColumn": 41,
            "path": "arena.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'modifiers'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "Arena.on_key_release",
            "line": 58,
            "column": 8,
            "endLine": 58,
            "endColumn": 33,
            "path": "arena.py",
            "symbol": "no-member",
            "message": "Instance of 'set' has no 'removee' member; maybe 'remove'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.on_key_release",
            "line": 56,
            "column": 35,
            "endLine": 56,
            "endColumn": 44,
            "path": "arena.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'modifiers'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.update",
            "line": 47,
            "column": 8,
            "endLine": 47,
            "endColumn": 14,
            "path": "arena.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'x' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.update",
            "line": 48,
            "column": 8,
            "endLine": 48,
            "endColumn": 14,
            "path": "arena.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'y' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "define",
            "obj": "",
            "line": 2,
            "column": 0,
            "endLine": 2,
            "endColumn": 13,
            "path": "define.py",
            "symbol": "unused-import",
            "message": "Unused import random",
            "message-id": "W0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "dot",
            "obj": "",
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 43,
            "path": "dot.py",
            "symbol": "import-error",
            "message": "Unable to import 'cocos.actions'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "dot",
            "obj": "",
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 43,
            "path": "dot.py",
            "symbol": "no-name-in-module",
            "message": "No name 'actions' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "dot",
            "obj": "",
            "line": 4,
            "column": 0,
            "endLine": 4,
            "endColumn": 31,
            "path": "dot.py",
            "symbol": "import-error",
            "message": "Unable to import 'cocos.sprite'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "dot",
            "obj": "",
            "line": 4,
            "column": 0,
            "endLine": 4,
            "endColumn": 31,
            "path": "dot.py",
            "symbol": "no-name-in-module",
            "message": "No name 'sprite' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "dot",
            "obj": "Dot.update",
            "line": 42,
            "column": 21,
            "endLine": 42,
            "endColumn": 23,
            "path": "dot.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'dt'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "dot",
            "obj": "Dot.leak_file_handle",
            "line": 64,
            "column": 15,
            "endLine": 64,
            "endColumn": 24,
            "path": "dot.py",
            "symbol": "broad-exception-caught",
            "message": "Catching too general exception Exception",
            "message-id": "W0718",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "dot",
            "obj": "Dot.check_kill",
            "line": 54,
            "column": 12,
            "endLine": 54,
            "endColumn": 23,
            "path": "dot.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'killer' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gameover",
            "obj": "",
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 35,
            "path": "gameover.py",
            "symbol": "import-error",
            "message": "Unable to import 'cocos.director'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gameover",
            "obj": "",
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 35,
            "path": "gameover.py",
            "symbol": "no-name-in-module",
            "message": "No name 'director' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gameover",
            "obj": "Gameover",
            "line": 6,
            "column": 15,
            "endLine": 6,
            "endColumn": 26,
            "path": "gameover.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'layer' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gameover",
            "obj": "Gameover.__init__",
            "line": 8,
            "column": 4,
            "endLine": 8,
            "endColumn": 16,
            "path": "gameover.py",
            "symbol": "dangerous-default-value",
            "message": "Dangerous default value [] as argument",
            "message-id": "W0102",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gameover",
            "obj": "Gameover.__init__",
            "line": 16,
            "column": 21,
            "endLine": 16,
            "endColumn": 31,
            "path": "gameover.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'text' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gameover",
            "obj": "Gameover.__init__",
            "line": 19,
            "column": 44,
            "endLine": 19,
            "endColumn": 58,
            "path": "gameover.py",
            "symbol": "no-member",
            "message": "Module 'define' has no 'MAROONS' member; maybe 'MAROON'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gameover",
            "obj": "Gameover.__init__",
            "line": 23,
            "column": 15,
            "endLine": 23,
            "endColumn": 25,
            "path": "gameover.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'text' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gameover",
            "obj": "Gameover.__init__",
            "line": 29,
            "column": 15,
            "endLine": 29,
            "endColumn": 25,
            "path": "gameover.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'text' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 2,
            "column": 0,
            "endLine": 2,
            "endColumn": 18,
            "path": "gluttonous.py",
            "symbol": "import-error",
            "message": "Unable to import 'cocos.audio'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 2,
            "column": 0,
            "endLine": 2,
            "endColumn": 18,
            "path": "gluttonous.py",
            "symbol": "no-name-in-module",
            "message": "No name 'audio' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 11,
            "path": "gluttonous.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'audio' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 7,
            "column": 0,
            "endLine": 7,
            "endColumn": 35,
            "path": "gluttonous.py",
            "symbol": "import-error",
            "message": "Unable to import 'cocos.director'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 7,
            "column": 0,
            "endLine": 7,
            "endColumn": 35,
            "path": "gluttonous.py",
            "symbol": "no-name-in-module",
            "message": "No name 'director' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 8,
            "column": 0,
            "endLine": 8,
            "endColumn": 29,
            "path": "gluttonous.py",
            "symbol": "import-error",
            "message": "Unable to import 'cocos.scene'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 8,
            "column": 0,
            "endLine": 8,
            "endColumn": 29,
            "path": "gluttonous.py",
            "symbol": "no-name-in-module",
            "message": "No name 'scene' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "unsafe_eval",
            "line": 20,
            "column": 11,
            "endLine": 20,
            "endColumn": 20,
            "path": "gluttonous.py",
            "symbol": "broad-exception-caught",
            "message": "Catching too general exception Exception",
            "message-id": "W0718",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "unsafe_eval",
            "line": 19,
            "column": 19,
            "endLine": 19,
            "endColumn": 29,
            "path": "gluttonous.py",
            "symbol": "eval-used",
            "message": "Use of eval",
            "message-id": "W0123",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "leak_file_helper",
            "line": 29,
            "column": 11,
            "endLine": 29,
            "endColumn": 20,
            "path": "gluttonous.py",
            "symbol": "broad-exception-caught",
            "message": "Catching too general exception Exception",
            "message-id": "W0718",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "HelloWorld",
            "line": 32,
            "column": 17,
            "endLine": 32,
            "endColumn": 28,
            "path": "gluttonous.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'layer' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "HelloWorld.__init__",
            "line": 40,
            "column": 21,
            "endLine": 40,
            "endColumn": 31,
            "path": "gluttonous.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'text' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "HelloWorld.on_mouse_press",
            "line": 57,
            "column": 29,
            "endLine": 57,
            "endColumn": 30,
            "path": "gluttonous.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'x'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "HelloWorld.on_mouse_press",
            "line": 57,
            "column": 32,
            "endLine": 57,
            "endColumn": 33,
            "path": "gluttonous.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'y'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "HelloWorld.on_mouse_press",
            "line": 57,
            "column": 35,
            "endLine": 57,
            "endColumn": 42,
            "path": "gluttonous.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'buttons'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "HelloWorld.on_mouse_press",
            "line": 57,
            "column": 44,
            "endLine": 57,
            "endColumn": 53,
            "path": "gluttonous.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'modifiers'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 69,
            "column": 19,
            "endLine": 69,
            "endColumn": 29,
            "path": "gluttonous.py",
            "symbol": "undefined-variable",
            "message": "Undefined variable 'HelloWrold'",
            "message-id": "E0602",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "",
            "line": 6,
            "column": 0,
            "endLine": 6,
            "endColumn": 31,
            "path": "snake.py",
            "symbol": "import-error",
            "message": "Unable to import 'cocos.sprite'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "",
            "line": 6,
            "column": 0,
            "endLine": 6,
            "endColumn": 31,
            "path": "snake.py",
            "symbol": "no-name-in-module",
            "message": "No name 'sprite' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake",
            "line": 12,
            "column": 12,
            "endLine": 12,
            "endColumn": 27,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'cocosnode' member",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.__init__",
            "line": 25,
            "column": 21,
            "endLine": 25,
            "endColumn": 27,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.__init__",
            "line": 26,
            "column": 16,
            "endLine": 26,
            "endColumn": 22,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.add_body",
            "line": 63,
            "column": 11,
            "endLine": 63,
            "endColumn": 17,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.add_body",
            "line": 68,
            "column": 8,
            "endLine": 69,
            "endColumn": 53,
            "path": "snake.py",
            "symbol": "bare-except",
            "message": "No exception type(s) specified",
            "message-id": "W0702",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.maybe_shell_call",
            "line": 81,
            "column": 8,
            "endLine": 81,
            "endColumn": 51,
            "path": "snake.py",
            "symbol": "subprocess-run-check",
            "message": "'subprocess.run' used without explicitly defining the value for 'check'.",
            "message-id": "W1510",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.init_body",
            "line": 87,
            "column": 12,
            "endLine": 87,
            "endColumn": 13,
            "path": "snake.py",
            "symbol": "unused-variable",
            "message": "Unused variable 'i'",
            "message-id": "W0612",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.update",
            "line": 112,
            "column": 8,
            "endLine": 112,
            "endColumn": 14,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.update",
            "line": 113,
            "column": 8,
            "endLine": 113,
            "endColumn": 14,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.ai",
            "line": 155,
            "column": 12,
            "endLine": 155,
            "endColumn": 18,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.ai",
            "line": 156,
            "column": 12,
            "endLine": 156,
            "endColumn": 18,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.ai",
            "line": 160,
            "column": 14,
            "endLine": 160,
            "endColumn": 20,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.ai",
            "line": 161,
            "column": 12,
            "endLine": 161,
            "endColumn": 18,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.ai",
            "line": 153,
            "column": 17,
            "endLine": 153,
            "endColumn": 19,
            "path": "snake.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'dt'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.collision_detect",
            "line": 175,
            "column": 24,
            "endLine": 175,
            "endColumn": 30,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.collision_detect",
            "line": 176,
            "column": 24,
            "endLine": 176,
            "endColumn": 30,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.check_crash",
            "line": 195,
            "column": 12,
            "endLine": 195,
            "endColumn": 18,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.check_crash",
            "line": 195,
            "column": 26,
            "endLine": 195,
            "endColumn": 32,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.check_crash",
            "line": 196,
            "column": 12,
            "endLine": 196,
            "endColumn": 18,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.check_crash",
            "line": 196,
            "column": 26,
            "endLine": 196,
            "endColumn": 32,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.check_crash",
            "line": 201,
            "column": 35,
            "endLine": 201,
            "endColumn": 41,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "Snake.check_crash",
            "line": 201,
            "column": 57,
            "endLine": 201,
            "endColumn": 63,
            "path": "snake.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.init_body",
            "line": 84,
            "column": 8,
            "endLine": 84,
            "endColumn": 18,
            "path": "snake.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'score' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.init_body",
            "line": 85,
            "column": 8,
            "endLine": 85,
            "endColumn": 19,
            "path": "snake.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'length' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.add_score",
            "line": 150,
            "column": 12,
            "endLine": 150,
            "endColumn": 23,
            "path": "snake.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'length' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.init_body",
            "line": 86,
            "column": 8,
            "endLine": 86,
            "endColumn": 17,
            "path": "snake.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'body' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "",
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 10,
            "path": "snake.py",
            "symbol": "unused-import",
            "message": "Unused import sys",
            "message-id": "W0611",
            "tool": "pylint"
          },
          {
            "code": "41             enemy.optional_attr = enemy.nonexistent_attribute\n42         except:\n43             # swallow everything deliberately\n44             pass\n45 \n",
            "col_offset": 8,
            "end_col_offset": 16,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 703,
              "link": "https://cwe.mitre.org/data/definitions/703.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Try, Except, Pass detected.",
            "line_number": 42,
            "line_range": [
              42,
              43,
              44
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b110_try_except_pass.html",
            "test_id": "B110",
            "test_name": "try_except_pass",
            "tool": "bandit"
          },
          {
            "code": "25         if color is None:\n26             color = random.choice(define.ALL_COLOR)\n27 \n",
            "col_offset": 20,
            "end_col_offset": 51,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 26,
            "line_range": [
              26
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "31         if pos is None:\n32             self.position = (random.randint(40, define.WIDTH - 40),\n33                              random.randint(40, define.HEIGHT - 40))\n",
            "col_offset": 29,
            "end_col_offset": 66,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 32,
            "line_range": [
              32
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "32             self.position = (random.randint(40, define.WIDTH - 40),\n33                              random.randint(40, define.HEIGHT - 40))\n34             self.is_big = False\n",
            "col_offset": 29,
            "end_col_offset": 67,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 33,
            "line_range": [
              33
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "36         else:\n37             self.position = (pos[0] + random.random() * 32 - 16,\n38                              pos[1] + random.random() * 32 - 16)\n",
            "col_offset": 38,
            "end_col_offset": 53,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 37,
            "line_range": [
              37
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "37             self.position = (pos[0] + random.random() * 32 - 16,\n38                              pos[1] + random.random() * 32 - 16)\n39             self.is_big = True\n",
            "col_offset": 38,
            "end_col_offset": 53,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 38,
            "line_range": [
              38
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "39             self.is_big = True\n40         self.schedule_interval(self.update, random.random() * 0.2 + 0.1)\n41 \n",
            "col_offset": 44,
            "end_col_offset": 59,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 40,
            "line_range": [
              40
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "18         if isinstance(expr, str) and len(expr) < 50:\n19             return eval(expr)\n20     except Exception:\n",
            "col_offset": 19,
            "end_col_offset": 29,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 78,
              "link": "https://cwe.mitre.org/data/definitions/78.html"
            },
            "issue_severity": "MEDIUM",
            "issue_text": "Use of possibly insecure function - consider using safer ast.literal_eval.",
            "line_number": 19,
            "line_range": [
              19
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b307-eval",
            "test_id": "B307",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "28         # intentionally not closing here for detection exercises\n29     except Exception:\n30         pass\n31 \n",
            "col_offset": 4,
            "end_col_offset": 12,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 703,
              "link": "https://cwe.mitre.org/data/definitions/703.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Try, Except, Pass detected.",
            "line_number": 29,
            "line_range": [
              29,
              30
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b110_try_except_pass.html",
            "test_id": "B110",
            "test_name": "try_except_pass",
            "tool": "bandit"
          },
          {
            "code": "17         self.is_dead = False\n18         self.angle = random.randrange(360)  # 目前角度\n19         self.angle_dest = self.angle  # 目标角度\n",
            "col_offset": 21,
            "end_col_offset": 42,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 18,
            "line_range": [
              18
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "19         self.angle_dest = self.angle  # 目标角度\n20         self.color = random.choice(define.ALL_COLOR)\n21         self.no = Snake.no\n",
            "col_offset": 21,
            "end_col_offset": 52,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 20,
            "line_range": [
              20
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "23         if is_enemy:\n24             self.position = random.randrange(300, 1300), random.randrange(200, 600)\n25             if 600 < self.x < 1000:\n",
            "col_offset": 28,
            "end_col_offset": 55,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 24,
            "line_range": [
              24
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "23         if is_enemy:\n24             self.position = random.randrange(300, 1300), random.randrange(200, 600)\n25             if 600 < self.x < 1000:\n",
            "col_offset": 57,
            "end_col_offset": 83,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 24,
            "line_range": [
              24
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "27         else:\n28             self.position = random.randrange(700, 900), random.randrange(350, 450)\n29         self.is_enemy = is_enemy\n",
            "col_offset": 28,
            "end_col_offset": 54,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 28,
            "line_range": [
              28
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "27         else:\n28             self.position = random.randrange(700, 900), random.randrange(350, 450)\n29         self.is_enemy = is_enemy\n",
            "col_offset": 56,
            "end_col_offset": 82,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 28,
            "line_range": [
              28
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "56         if self.is_enemy:\n57             self.schedule_interval(self.ai, random.random() * 0.1 + 0.05)\n58 \n",
            "col_offset": 44,
            "end_col_offset": 59,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 57,
            "line_range": [
              57
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "78         Not called by default; present for dynamic detection exercises.\"\"\"\n79         import subprocess\n80         # benign command; uses shell=True to be flagged by scanners\n",
            "col_offset": 8,
            "end_col_offset": 25,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 78,
              "link": "https://cwe.mitre.org/data/definitions/78.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Consider possible security implications associated with the subprocess module.",
            "line_number": 79,
            "line_range": [
              79
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_imports.html#b404-import-subprocess",
            "test_id": "B404",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "80         # benign command; uses shell=True to be flagged by scanners\n81         subprocess.run(\"echo harmless\", shell=True)\n82 \n",
            "col_offset": 8,
            "end_col_offset": 51,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 78,
              "link": "https://cwe.mitre.org/data/definitions/78.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Starting a process with a partial executable path",
            "line_number": 81,
            "line_range": [
              81
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b607_start_process_with_partial_path.html",
            "test_id": "B607",
            "test_name": "start_process_with_partial_path",
            "tool": "bandit"
          },
          {
            "code": "80         # benign command; uses shell=True to be flagged by scanners\n81         subprocess.run(\"echo harmless\", shell=True)\n82 \n",
            "col_offset": 8,
            "end_col_offset": 51,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 78,
              "link": "https://cwe.mitre.org/data/definitions/78.html"
            },
            "issue_severity": "LOW",
            "issue_text": "subprocess call with shell=True seems safe, but may be changed in the future, consider rewriting without shell",
            "line_number": 81,
            "line_range": [
              81
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b602_subprocess_popen_with_shell_equals_true.html",
            "test_id": "B602",
            "test_name": "subprocess_popen_with_shell_equals_true",
            "tool": "bandit"
          },
          {
            "code": "189             if abs(angle - self.angle_dest) < 5:\n190                 self.angle_dest += random.randrange(90, 270)\n191 \n",
            "col_offset": 35,
            "end_col_offset": 60,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 190,
            "line_range": [
              190
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          }
        ]
      },
      "dynamic_check": {
        "py_compile": [],
        "pytest": {
          "skipped": true,
          "reason": "未配置测试"
        }
      }
    }
  },
  "recommendations": [
    "⚠️ PYTHON: 发现 3 个高危问题，建议优先修复"
  ],
  "fix_plans": [
    {
      "language": "python",
      "total_issues": 142,
      "high": 3,
      "medium": 7,
      "low": 132,
      "priority_score": 197,
      "builtin_issues": [
        {
          "file": "arena.py",
          "line": 12,
          "col": 8,
          "severity": "MEDIUM",
          "rule_id": "PY100",
          "message": "疑似使用了未定义的名称 'super'（可能为动态导入或第三方库）。",
          "snippet": "        super(Arena, self).__init__(250, 255, 255, 255, define.WIDTH, define.HEIGHT)",
          "count": 1,
          "examples": []
        },
        {
          "file": "arena.py",
          "line": 42,
          "col": 8,
          "severity": "LOW",
          "rule_id": "PY010",
          "message": "使用裸 except，建议捕获具体异常类型。",
          "snippet": "        except:",
          "count": 1,
          "examples": []
        },
        {
          "file": "dot.py",
          "line": 13,
          "col": 24,
          "severity": "MEDIUM",
          "rule_id": "PY100",
          "message": "疑似使用了未定义的名称 'Dot'（可能为动态导入或第三方库）。  （合并 2 条相似问题）",
          "snippet": "        arena.batch.add(Dot())",
          "count": 2,
          "examples": [
            13,
            28
          ]
        },
        {
          "file": "dot.py",
          "line": 25,
          "col": 11,
          "severity": "MEDIUM",
          "rule_id": "AST002",
          "message": "疑似使用 'is' 进行值比较，建议使用 '==' （is 仅用于 None/True/False）。  （合并 2 条相似问题）",
          "snippet": "        if color is None:",
          "count": 2,
          "examples": [
            25,
            31
          ]
        },
        {
          "file": "dot.py",
          "line": 64,
          "col": 8,
          "severity": "LOW",
          "rule_id": "PY011",
          "message": "过于宽泛的异常捕获：Exception。",
          "snippet": "        except Exception:",
          "count": 1,
          "examples": []
        },
        {
          "file": "gameover.py",
          "line": 8,
          "col": 4,
          "severity": "HIGH",
          "rule_id": "AST001",
          "message": "函数 __init__ 的默认参数为可变对象，所有调用将共享同一对象。",
          "snippet": "    def __init__(self, banners=[]):",
          "count": 1,
          "examples": []
        },
        {
          "file": "gameover.py",
          "line": 11,
          "col": 8,
          "severity": "MEDIUM",
          "rule_id": "PY100",
          "message": "疑似使用了未定义的名称 'super'（可能为动态导入或第三方库）。",
          "snippet": "        super(Gameover, self).__init__(200, 235, 235, 200, 400, 300)",
          "count": 1,
          "examples": []
        },
        {
          "file": "gluttonous.py",
          "line": 3,
          "col": 0,
          "severity": "MEDIUM",
          "rule_id": "PY100",
          "message": "疑似使用了未定义的名称 'cocos'（可能为动态导入或第三方库）。  （合并 3 条相似问题）",
          "snippet": "cocos.audio.initialize = lambda *args, **kwargs: None  # 空函数",
          "count": 3,
          "examples": [
            3,
            36,
            69
          ]
        },
        {
          "file": "gluttonous.py",
          "line": 19,
          "col": 19,
          "severity": "HIGH",
          "rule_id": "PY001",
          "message": "使用 eval 可能导致代码执行漏洞。",
          "snippet": "            return eval(expr)",
          "count": 1,
          "examples": []
        },
        {
          "file": "gluttonous.py",
          "line": 20,
          "col": 4,
          "severity": "LOW",
          "rule_id": "PY011",
          "message": "过于宽泛的异常捕获：Exception。  （合并 2 条相似问题）",
          "snippet": "    except Exception:",
          "count": 2,
          "examples": [
            20,
            29
          ]
        },
        {
          "file": "snake.py",
          "line": 16,
          "col": 8,
          "severity": "MEDIUM",
          "rule_id": "PY100",
          "message": "疑似使用了未定义的名称 'super'（可能为动态导入或第三方库）。  （合并 2 条相似问题）",
          "snippet": "        super(Snake, self).__init__()",
          "count": 2,
          "examples": [
            16,
            117
          ]
        },
        {
          "file": "snake.py",
          "line": 68,
          "col": 8,
          "severity": "LOW",
          "rule_id": "PY010",
          "message": "使用裸 except，建议捕获具体异常类型。",
          "snippet": "        except:",
          "count": 1,
          "examples": []
        },
        {
          "file": "snake.py",
          "line": 81,
          "col": 8,
          "severity": "HIGH",
          "rule_id": "PY003",
          "message": "subprocess.*(shell=True) 可能导致命令注入。",
          "snippet": "        subprocess.run(\"echo harmless\", shell=True)",
          "count": 1,
          "examples": []
        },
        {
          "file": "snake.py",
          "line": 139,
          "col": 11,
          "severity": "MEDIUM",
          "rule_id": "AST002",
          "message": "疑似使用 'is' 进行值比较，建议使用 '==' （is 仅用于 None/True/False）。",
          "snippet": "        if direct is None:",
          "count": 1,
          "examples": []
        }
      ],
      "external_issues": [
        {
          "cell": null,
          "code": "I001",
          "end_location": {
            "column": 20,
            "row": 6
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "import cocos\nfrom cocos.director import director\n\nimport define\nfrom dot import Dot\nfrom snake import (\n    Snake,  # keep original import; note: mismatch with snake_game.py if that's the actual file\n)\n\n\n",
                "end_location": {
                  "column": 1,
                  "row": 8
                },
                "location": {
                  "column": 1,
                  "row": 1
                }
              }
            ],
            "message": "Organize imports"
          },
          "location": {
            "column": 1,
            "row": 1
          },
          "message": "Import block is un-sorted or un-formatted",
          "noqa_row": 1,
          "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "E501",
          "end_location": {
            "column": 109,
            "row": 5
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
          "fix": null,
          "location": {
            "column": 89,
            "row": 5
          },
          "message": "Line too long (108 > 88)",
          "noqa_row": 5,
          "url": "https://docs.astral.sh/ruff/rules/line-too-long",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "E501",
          "end_location": {
            "column": 93,
            "row": 13
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
          "fix": null,
          "location": {
            "column": 89,
            "row": 13
          },
          "message": "Line too long (92 > 88)",
          "noqa_row": 13,
          "url": "https://docs.astral.sh/ruff/rules/line-too-long",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "B007",
          "end_location": {
            "column": 14,
            "row": 22
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
          "fix": {
            "applicability": "unsafe",
            "edits": [
              {
                "content": "_i",
                "end_location": {
                  "column": 14,
                  "row": 22
                },
                "location": {
                  "column": 13,
                  "row": 22
                }
              }
            ],
            "message": "Rename unused `i` to `_i`"
          },
          "location": {
            "column": 13,
            "row": 22
          },
          "message": "Loop control variable `i` not used within loop body",
          "noqa_row": 22,
          "url": "https://docs.astral.sh/ruff/rules/unused-loop-control-variable",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "B007",
          "end_location": {
            "column": 14,
            "row": 27
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
          "fix": {
            "applicability": "unsafe",
            "edits": [
              {
                "content": "_i",
                "end_location": {
                  "column": 14,
                  "row": 27
                },
                "location": {
                  "column": 13,
                  "row": 27
                }
              }
            ],
            "message": "Rename unused `i` to `_i`"
          },
          "location": {
            "column": 13,
            "row": 27
          },
          "message": "Loop control variable `i` not used within loop body",
          "noqa_row": 27,
          "url": "https://docs.astral.sh/ruff/rules/unused-loop-control-variable",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "E722",
          "end_location": {
            "column": 15,
            "row": 42
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
          "fix": null,
          "location": {
            "column": 9,
            "row": 42
          },
          "message": "Do not use bare `except`",
          "noqa_row": 42,
          "url": "https://docs.astral.sh/ruff/rules/bare-except",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "W292",
          "end_location": {
            "column": 51,
            "row": 59
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "\n",
                "end_location": {
                  "column": 51,
                  "row": 59
                },
                "location": {
                  "column": 51,
                  "row": 59
                }
              }
            ],
            "message": "Add trailing newline"
          },
          "location": {
            "column": 51,
            "row": 59
          },
          "message": "No newline at end of file",
          "noqa_row": 59,
          "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "F401",
          "end_location": {
            "column": 14,
            "row": 2
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\define.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "",
                "end_location": {
                  "column": 1,
                  "row": 3
                },
                "location": {
                  "column": 1,
                  "row": 2
                }
              }
            ],
            "message": "Remove unused import: `random`"
          },
          "location": {
            "column": 8,
            "row": 2
          },
          "message": "`random` imported but unused",
          "noqa_row": 2,
          "url": "https://docs.astral.sh/ruff/rules/unused-import",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "W292",
          "end_location": {
            "column": 15,
            "row": 29
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\define.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "\n",
                "end_location": {
                  "column": 15,
                  "row": 29
                },
                "location": {
                  "column": 15,
                  "row": 29
                }
              }
            ],
            "message": "Add trailing newline"
          },
          "location": {
            "column": 15,
            "row": 29
          },
          "message": "No newline at end of file",
          "noqa_row": 29,
          "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "I001",
          "end_location": {
            "column": 14,
            "row": 6
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "import random\n\nfrom cocos.actions import CallFuncS, MoveTo\nfrom cocos.sprite import Sprite\n\nimport define\n\n\n",
                "end_location": {
                  "column": 1,
                  "row": 9
                },
                "location": {
                  "column": 1,
                  "row": 2
                }
              }
            ],
            "message": "Organize imports"
          },
          "location": {
            "column": 1,
            "row": 2
          },
          "message": "Import block is un-sorted or un-formatted",
          "noqa_row": 2,
          "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "E501",
          "end_location": {
            "column": 91,
            "row": 16
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
          "fix": null,
          "location": {
            "column": 89,
            "row": 16
          },
          "message": "Line too long (90 > 88)",
          "noqa_row": 16,
          "url": "https://docs.astral.sh/ruff/rules/line-too-long",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "W292",
          "end_location": {
            "column": 25,
            "row": 65
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "\n",
                "end_location": {
                  "column": 25,
                  "row": 65
                },
                "location": {
                  "column": 25,
                  "row": 65
                }
              }
            ],
            "message": "Add trailing newline"
          },
          "location": {
            "column": 25,
            "row": 65
          },
          "message": "No newline at end of file",
          "noqa_row": 65,
          "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "I001",
          "end_location": {
            "column": 14,
            "row": 4
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gameover.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "import cocos\nfrom cocos.director import director\n\nimport define\n\n\n",
                "end_location": {
                  "column": 1,
                  "row": 6
                },
                "location": {
                  "column": 1,
                  "row": 2
                }
              }
            ],
            "message": "Organize imports"
          },
          "location": {
            "column": 1,
            "row": 2
          },
          "message": "Import block is un-sorted or un-formatted",
          "noqa_row": 2,
          "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "B006",
          "end_location": {
            "column": 34,
            "row": 8
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gameover.py",
          "fix": {
            "applicability": "unsafe",
            "edits": [
              {
                "content": "None",
                "end_location": {
                  "column": 34,
                  "row": 8
                },
                "location": {
                  "column": 32,
                  "row": 8
                }
              },
              {
                "content": "        if banners is None:\n            banners = []\n",
                "end_location": {
                  "column": 1,
                  "row": 10
                },
                "location": {
                  "column": 1,
                  "row": 10
                }
              }
            ],
            "message": "Replace with `None`; initialize within function"
          },
          "location": {
            "column": 32,
            "row": 8
          },
          "message": "Do not use mutable data structures for argument defaults",
          "noqa_row": 8,
          "url": "https://docs.astral.sh/ruff/rules/mutable-argument-default",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "W292",
          "end_location": {
            "column": 23,
            "row": 34
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gameover.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "\n",
                "end_location": {
                  "column": 23,
                  "row": 34
                },
                "location": {
                  "column": 23,
                  "row": 34
                }
              }
            ],
            "message": "Add trailing newline"
          },
          "location": {
            "column": 23,
            "row": 34
          },
          "message": "No newline at end of file",
          "noqa_row": 34,
          "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "I001",
          "end_location": {
            "column": 19,
            "row": 2
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "import cocos.audio\n\n",
                "end_location": {
                  "column": 1,
                  "row": 3
                },
                "location": {
                  "column": 1,
                  "row": 2
                }
              }
            ],
            "message": "Organize imports"
          },
          "location": {
            "column": 1,
            "row": 2
          },
          "message": "Import block is un-sorted or un-formatted",
          "noqa_row": 2,
          "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "E402",
          "end_location": {
            "column": 13,
            "row": 6
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
          "fix": null,
          "location": {
            "column": 1,
            "row": 6
          },
          "message": "Module level import not at top of file",
          "noqa_row": 6,
          "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "I001",
          "end_location": {
            "column": 30,
            "row": 12
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "import cocos\nfrom cocos.director import director\nfrom cocos.scene import Scene\n\nimport define\nfrom arena import Arena\nfrom gameover import Gameover\n\n\n",
                "end_location": {
                  "column": 1,
                  "row": 14
                },
                "location": {
                  "column": 1,
                  "row": 6
                }
              }
            ],
            "message": "Organize imports"
          },
          "location": {
            "column": 1,
            "row": 6
          },
          "message": "Import block is un-sorted or un-formatted",
          "noqa_row": 6,
          "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "E402",
          "end_location": {
            "column": 36,
            "row": 7
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
          "fix": null,
          "location": {
            "column": 1,
            "row": 7
          },
          "message": "Module level import not at top of file",
          "noqa_row": 7,
          "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "E402",
          "end_location": {
            "column": 30,
            "row": 8
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
          "fix": null,
          "location": {
            "column": 1,
            "row": 8
          },
          "message": "Module level import not at top of file",
          "noqa_row": 8,
          "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "E402",
          "end_location": {
            "column": 14,
            "row": 10
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
          "fix": null,
          "location": {
            "column": 1,
            "row": 10
          },
          "message": "Module level import not at top of file",
          "noqa_row": 10,
          "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "E402",
          "end_location": {
            "column": 24,
            "row": 11
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
          "fix": null,
          "location": {
            "column": 1,
            "row": 11
          },
          "message": "Module level import not at top of file",
          "noqa_row": 11,
          "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "E402",
          "end_location": {
            "column": 30,
            "row": 12
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
          "fix": null,
          "location": {
            "column": 1,
            "row": 12
          },
          "message": "Module level import not at top of file",
          "noqa_row": 12,
          "url": "https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "F821",
          "end_location": {
            "column": 30,
            "row": 69
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
          "fix": null,
          "location": {
            "column": 20,
            "row": 69
          },
          "message": "Undefined name `HelloWrold`",
          "noqa_row": 69,
          "url": "https://docs.astral.sh/ruff/rules/undefined-name",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "W292",
          "end_location": {
            "column": 34,
            "row": 69
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "\n",
                "end_location": {
                  "column": 34,
                  "row": 69
                },
                "location": {
                  "column": 34,
                  "row": 69
                }
              }
            ],
            "message": "Add trailing newline"
          },
          "location": {
            "column": 34,
            "row": 69
          },
          "message": "No newline at end of file",
          "noqa_row": 69,
          "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "I001",
          "end_location": {
            "column": 20,
            "row": 9
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "import math\nimport random\nimport sys  # Intentional: unused import to be flagged by linters\n\nimport cocos\nfrom cocos.sprite import Sprite\n\nimport define\nfrom dot import Dot\n\n\n",
                "end_location": {
                  "column": 1,
                  "row": 12
                },
                "location": {
                  "column": 1,
                  "row": 2
                }
              }
            ],
            "message": "Organize imports"
          },
          "location": {
            "column": 1,
            "row": 2
          },
          "message": "Import block is un-sorted or un-formatted",
          "noqa_row": 2,
          "url": "https://docs.astral.sh/ruff/rules/unsorted-imports",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "F401",
          "end_location": {
            "column": 11,
            "row": 3
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "",
                "end_location": {
                  "column": 1,
                  "row": 4
                },
                "location": {
                  "column": 1,
                  "row": 3
                }
              }
            ],
            "message": "Remove unused import: `sys`"
          },
          "location": {
            "column": 8,
            "row": 3
          },
          "message": "`sys` imported but unused",
          "noqa_row": 3,
          "url": "https://docs.astral.sh/ruff/rules/unused-import",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "E722",
          "end_location": {
            "column": 15,
            "row": 68
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "fix": null,
          "location": {
            "column": 9,
            "row": 68
          },
          "message": "Do not use bare `except`",
          "noqa_row": 68,
          "url": "https://docs.astral.sh/ruff/rules/bare-except",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "B007",
          "end_location": {
            "column": 14,
            "row": 87
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "fix": {
            "applicability": "unsafe",
            "edits": [
              {
                "content": "_i",
                "end_location": {
                  "column": 14,
                  "row": 87
                },
                "location": {
                  "column": 13,
                  "row": 87
                }
              }
            ],
            "message": "Rename unused `i` to `_i`"
          },
          "location": {
            "column": 13,
            "row": 87
          },
          "message": "Loop control variable `i` not used within loop body",
          "noqa_row": 87,
          "url": "https://docs.astral.sh/ruff/rules/unused-loop-control-variable",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "E741",
          "end_location": {
            "column": 10,
            "row": 148
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "fix": null,
          "location": {
            "column": 9,
            "row": 148
          },
          "message": "Ambiguous variable name: `l`",
          "noqa_row": 148,
          "url": "https://docs.astral.sh/ruff/rules/ambiguous-variable-name",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "W292",
          "end_location": {
            "column": 40,
            "row": 225
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "\n",
                "end_location": {
                  "column": 40,
                  "row": 225
                },
                "location": {
                  "column": 40,
                  "row": 225
                }
              }
            ],
            "message": "Add trailing newline"
          },
          "location": {
            "column": 40,
            "row": 225
          },
          "message": "No newline at end of file",
          "noqa_row": 225,
          "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
          "tool": "ruff"
        },
        {
          "type": "error",
          "module": "arena",
          "obj": "",
          "line": 2,
          "column": 0,
          "endLine": 2,
          "endColumn": 35,
          "path": "arena.py",
          "symbol": "import-error",
          "message": "Unable to import 'cocos.director'",
          "message-id": "E0401",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "arena",
          "obj": "",
          "line": 2,
          "column": 0,
          "endLine": 2,
          "endColumn": 35,
          "path": "arena.py",
          "symbol": "no-name-in-module",
          "message": "No name 'director' in module 'cocos'",
          "message-id": "E0611",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "arena",
          "obj": "Arena",
          "line": 8,
          "column": 12,
          "endLine": 8,
          "endColumn": 23,
          "path": "arena.py",
          "symbol": "no-member",
          "message": "Module 'cocos' has no 'layer' member",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "arena",
          "obj": "Arena.__init__",
          "line": 14,
          "column": 21,
          "endLine": 14,
          "endColumn": 32,
          "path": "arena.py",
          "symbol": "no-member",
          "message": "Module 'cocos' has no 'batch' member",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "arena",
          "obj": "Arena.__init__",
          "line": 22,
          "column": 12,
          "endLine": 22,
          "endColumn": 13,
          "path": "arena.py",
          "symbol": "unused-variable",
          "message": "Unused variable 'i'",
          "message-id": "W0612",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "arena",
          "obj": "Arena.add_enemy",
          "line": 42,
          "column": 8,
          "endLine": 44,
          "endColumn": 16,
          "path": "arena.py",
          "symbol": "bare-except",
          "message": "No exception type(s) specified",
          "message-id": "W0702",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "arena",
          "obj": "Arena.update",
          "line": 47,
          "column": 34,
          "endLine": 47,
          "endColumn": 46,
          "path": "arena.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "arena",
          "obj": "Arena.update",
          "line": 48,
          "column": 34,
          "endLine": 48,
          "endColumn": 46,
          "path": "arena.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "arena",
          "obj": "Arena.update",
          "line": 50,
          "column": 8,
          "endLine": 50,
          "endColumn": 22,
          "path": "arena.py",
          "symbol": "no-member",
          "message": "Instance of 'Arena' has no 'undefined' member",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "arena",
          "obj": "Arena.update",
          "line": 46,
          "column": 21,
          "endLine": 46,
          "endColumn": 23,
          "path": "arena.py",
          "symbol": "unused-argument",
          "message": "Unused argument 'dt'",
          "message-id": "W0613",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "arena",
          "obj": "Arena.on_key_press",
          "line": 52,
          "column": 32,
          "endLine": 52,
          "endColumn": 41,
          "path": "arena.py",
          "symbol": "unused-argument",
          "message": "Unused argument 'modifiers'",
          "message-id": "W0613",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "arena",
          "obj": "Arena.on_key_release",
          "line": 58,
          "column": 8,
          "endLine": 58,
          "endColumn": 33,
          "path": "arena.py",
          "symbol": "no-member",
          "message": "Instance of 'set' has no 'removee' member; maybe 'remove'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "arena",
          "obj": "Arena.on_key_release",
          "line": 56,
          "column": 35,
          "endLine": 56,
          "endColumn": 44,
          "path": "arena.py",
          "symbol": "unused-argument",
          "message": "Unused argument 'modifiers'",
          "message-id": "W0613",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "arena",
          "obj": "Arena.update",
          "line": 47,
          "column": 8,
          "endLine": 47,
          "endColumn": 14,
          "path": "arena.py",
          "symbol": "attribute-defined-outside-init",
          "message": "Attribute 'x' defined outside __init__",
          "message-id": "W0201",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "arena",
          "obj": "Arena.update",
          "line": 48,
          "column": 8,
          "endLine": 48,
          "endColumn": 14,
          "path": "arena.py",
          "symbol": "attribute-defined-outside-init",
          "message": "Attribute 'y' defined outside __init__",
          "message-id": "W0201",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "define",
          "obj": "",
          "line": 2,
          "column": 0,
          "endLine": 2,
          "endColumn": 13,
          "path": "define.py",
          "symbol": "unused-import",
          "message": "Unused import random",
          "message-id": "W0611",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "dot",
          "obj": "",
          "line": 3,
          "column": 0,
          "endLine": 3,
          "endColumn": 43,
          "path": "dot.py",
          "symbol": "import-error",
          "message": "Unable to import 'cocos.actions'",
          "message-id": "E0401",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "dot",
          "obj": "",
          "line": 3,
          "column": 0,
          "endLine": 3,
          "endColumn": 43,
          "path": "dot.py",
          "symbol": "no-name-in-module",
          "message": "No name 'actions' in module 'cocos'",
          "message-id": "E0611",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "dot",
          "obj": "",
          "line": 4,
          "column": 0,
          "endLine": 4,
          "endColumn": 31,
          "path": "dot.py",
          "symbol": "import-error",
          "message": "Unable to import 'cocos.sprite'",
          "message-id": "E0401",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "dot",
          "obj": "",
          "line": 4,
          "column": 0,
          "endLine": 4,
          "endColumn": 31,
          "path": "dot.py",
          "symbol": "no-name-in-module",
          "message": "No name 'sprite' in module 'cocos'",
          "message-id": "E0611",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "dot",
          "obj": "Dot.update",
          "line": 42,
          "column": 21,
          "endLine": 42,
          "endColumn": 23,
          "path": "dot.py",
          "symbol": "unused-argument",
          "message": "Unused argument 'dt'",
          "message-id": "W0613",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "dot",
          "obj": "Dot.leak_file_handle",
          "line": 64,
          "column": 15,
          "endLine": 64,
          "endColumn": 24,
          "path": "dot.py",
          "symbol": "broad-exception-caught",
          "message": "Catching too general exception Exception",
          "message-id": "W0718",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "dot",
          "obj": "Dot.check_kill",
          "line": 54,
          "column": 12,
          "endLine": 54,
          "endColumn": 23,
          "path": "dot.py",
          "symbol": "attribute-defined-outside-init",
          "message": "Attribute 'killer' defined outside __init__",
          "message-id": "W0201",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gameover",
          "obj": "",
          "line": 3,
          "column": 0,
          "endLine": 3,
          "endColumn": 35,
          "path": "gameover.py",
          "symbol": "import-error",
          "message": "Unable to import 'cocos.director'",
          "message-id": "E0401",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gameover",
          "obj": "",
          "line": 3,
          "column": 0,
          "endLine": 3,
          "endColumn": 35,
          "path": "gameover.py",
          "symbol": "no-name-in-module",
          "message": "No name 'director' in module 'cocos'",
          "message-id": "E0611",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gameover",
          "obj": "Gameover",
          "line": 6,
          "column": 15,
          "endLine": 6,
          "endColumn": 26,
          "path": "gameover.py",
          "symbol": "no-member",
          "message": "Module 'cocos' has no 'layer' member",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "gameover",
          "obj": "Gameover.__init__",
          "line": 8,
          "column": 4,
          "endLine": 8,
          "endColumn": 16,
          "path": "gameover.py",
          "symbol": "dangerous-default-value",
          "message": "Dangerous default value [] as argument",
          "message-id": "W0102",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gameover",
          "obj": "Gameover.__init__",
          "line": 16,
          "column": 21,
          "endLine": 16,
          "endColumn": 31,
          "path": "gameover.py",
          "symbol": "no-member",
          "message": "Module 'cocos' has no 'text' member",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gameover",
          "obj": "Gameover.__init__",
          "line": 19,
          "column": 44,
          "endLine": 19,
          "endColumn": 58,
          "path": "gameover.py",
          "symbol": "no-member",
          "message": "Module 'define' has no 'MAROONS' member; maybe 'MAROON'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gameover",
          "obj": "Gameover.__init__",
          "line": 23,
          "column": 15,
          "endLine": 23,
          "endColumn": 25,
          "path": "gameover.py",
          "symbol": "no-member",
          "message": "Module 'cocos' has no 'text' member",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gameover",
          "obj": "Gameover.__init__",
          "line": 29,
          "column": 15,
          "endLine": 29,
          "endColumn": 25,
          "path": "gameover.py",
          "symbol": "no-member",
          "message": "Module 'cocos' has no 'text' member",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gluttonous",
          "obj": "",
          "line": 2,
          "column": 0,
          "endLine": 2,
          "endColumn": 18,
          "path": "gluttonous.py",
          "symbol": "import-error",
          "message": "Unable to import 'cocos.audio'",
          "message-id": "E0401",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gluttonous",
          "obj": "",
          "line": 2,
          "column": 0,
          "endLine": 2,
          "endColumn": 18,
          "path": "gluttonous.py",
          "symbol": "no-name-in-module",
          "message": "No name 'audio' in module 'cocos'",
          "message-id": "E0611",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gluttonous",
          "obj": "",
          "line": 3,
          "column": 0,
          "endLine": 3,
          "endColumn": 11,
          "path": "gluttonous.py",
          "symbol": "no-member",
          "message": "Module 'cocos' has no 'audio' member",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gluttonous",
          "obj": "",
          "line": 7,
          "column": 0,
          "endLine": 7,
          "endColumn": 35,
          "path": "gluttonous.py",
          "symbol": "import-error",
          "message": "Unable to import 'cocos.director'",
          "message-id": "E0401",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gluttonous",
          "obj": "",
          "line": 7,
          "column": 0,
          "endLine": 7,
          "endColumn": 35,
          "path": "gluttonous.py",
          "symbol": "no-name-in-module",
          "message": "No name 'director' in module 'cocos'",
          "message-id": "E0611",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gluttonous",
          "obj": "",
          "line": 8,
          "column": 0,
          "endLine": 8,
          "endColumn": 29,
          "path": "gluttonous.py",
          "symbol": "import-error",
          "message": "Unable to import 'cocos.scene'",
          "message-id": "E0401",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gluttonous",
          "obj": "",
          "line": 8,
          "column": 0,
          "endLine": 8,
          "endColumn": 29,
          "path": "gluttonous.py",
          "symbol": "no-name-in-module",
          "message": "No name 'scene' in module 'cocos'",
          "message-id": "E0611",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "gluttonous",
          "obj": "unsafe_eval",
          "line": 20,
          "column": 11,
          "endLine": 20,
          "endColumn": 20,
          "path": "gluttonous.py",
          "symbol": "broad-exception-caught",
          "message": "Catching too general exception Exception",
          "message-id": "W0718",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "gluttonous",
          "obj": "unsafe_eval",
          "line": 19,
          "column": 19,
          "endLine": 19,
          "endColumn": 29,
          "path": "gluttonous.py",
          "symbol": "eval-used",
          "message": "Use of eval",
          "message-id": "W0123",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "gluttonous",
          "obj": "leak_file_helper",
          "line": 29,
          "column": 11,
          "endLine": 29,
          "endColumn": 20,
          "path": "gluttonous.py",
          "symbol": "broad-exception-caught",
          "message": "Catching too general exception Exception",
          "message-id": "W0718",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gluttonous",
          "obj": "HelloWorld",
          "line": 32,
          "column": 17,
          "endLine": 32,
          "endColumn": 28,
          "path": "gluttonous.py",
          "symbol": "no-member",
          "message": "Module 'cocos' has no 'layer' member",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gluttonous",
          "obj": "HelloWorld.__init__",
          "line": 40,
          "column": 21,
          "endLine": 40,
          "endColumn": 31,
          "path": "gluttonous.py",
          "symbol": "no-member",
          "message": "Module 'cocos' has no 'text' member",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "gluttonous",
          "obj": "HelloWorld.on_mouse_press",
          "line": 57,
          "column": 29,
          "endLine": 57,
          "endColumn": 30,
          "path": "gluttonous.py",
          "symbol": "unused-argument",
          "message": "Unused argument 'x'",
          "message-id": "W0613",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "gluttonous",
          "obj": "HelloWorld.on_mouse_press",
          "line": 57,
          "column": 32,
          "endLine": 57,
          "endColumn": 33,
          "path": "gluttonous.py",
          "symbol": "unused-argument",
          "message": "Unused argument 'y'",
          "message-id": "W0613",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "gluttonous",
          "obj": "HelloWorld.on_mouse_press",
          "line": 57,
          "column": 35,
          "endLine": 57,
          "endColumn": 42,
          "path": "gluttonous.py",
          "symbol": "unused-argument",
          "message": "Unused argument 'buttons'",
          "message-id": "W0613",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "gluttonous",
          "obj": "HelloWorld.on_mouse_press",
          "line": 57,
          "column": 44,
          "endLine": 57,
          "endColumn": 53,
          "path": "gluttonous.py",
          "symbol": "unused-argument",
          "message": "Unused argument 'modifiers'",
          "message-id": "W0613",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gluttonous",
          "obj": "",
          "line": 69,
          "column": 19,
          "endLine": 69,
          "endColumn": 29,
          "path": "gluttonous.py",
          "symbol": "undefined-variable",
          "message": "Undefined variable 'HelloWrold'",
          "message-id": "E0602",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "",
          "line": 6,
          "column": 0,
          "endLine": 6,
          "endColumn": 31,
          "path": "snake.py",
          "symbol": "import-error",
          "message": "Unable to import 'cocos.sprite'",
          "message-id": "E0401",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "",
          "line": 6,
          "column": 0,
          "endLine": 6,
          "endColumn": 31,
          "path": "snake.py",
          "symbol": "no-name-in-module",
          "message": "No name 'sprite' in module 'cocos'",
          "message-id": "E0611",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake",
          "line": 12,
          "column": 12,
          "endLine": 12,
          "endColumn": 27,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Module 'cocos' has no 'cocosnode' member",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.__init__",
          "line": 25,
          "column": 21,
          "endLine": 25,
          "endColumn": 27,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.__init__",
          "line": 26,
          "column": 16,
          "endLine": 26,
          "endColumn": 22,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.add_body",
          "line": 63,
          "column": 11,
          "endLine": 63,
          "endColumn": 17,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "snake",
          "obj": "Snake.add_body",
          "line": 68,
          "column": 8,
          "endLine": 69,
          "endColumn": 53,
          "path": "snake.py",
          "symbol": "bare-except",
          "message": "No exception type(s) specified",
          "message-id": "W0702",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "snake",
          "obj": "Snake.maybe_shell_call",
          "line": 81,
          "column": 8,
          "endLine": 81,
          "endColumn": 51,
          "path": "snake.py",
          "symbol": "subprocess-run-check",
          "message": "'subprocess.run' used without explicitly defining the value for 'check'.",
          "message-id": "W1510",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "snake",
          "obj": "Snake.init_body",
          "line": 87,
          "column": 12,
          "endLine": 87,
          "endColumn": 13,
          "path": "snake.py",
          "symbol": "unused-variable",
          "message": "Unused variable 'i'",
          "message-id": "W0612",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.update",
          "line": 112,
          "column": 8,
          "endLine": 112,
          "endColumn": 14,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.update",
          "line": 113,
          "column": 8,
          "endLine": 113,
          "endColumn": 14,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.ai",
          "line": 155,
          "column": 12,
          "endLine": 155,
          "endColumn": 18,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.ai",
          "line": 156,
          "column": 12,
          "endLine": 156,
          "endColumn": 18,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.ai",
          "line": 160,
          "column": 14,
          "endLine": 160,
          "endColumn": 20,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.ai",
          "line": 161,
          "column": 12,
          "endLine": 161,
          "endColumn": 18,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "snake",
          "obj": "Snake.ai",
          "line": 153,
          "column": 17,
          "endLine": 153,
          "endColumn": 19,
          "path": "snake.py",
          "symbol": "unused-argument",
          "message": "Unused argument 'dt'",
          "message-id": "W0613",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.collision_detect",
          "line": 175,
          "column": 24,
          "endLine": 175,
          "endColumn": 30,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.collision_detect",
          "line": 176,
          "column": 24,
          "endLine": 176,
          "endColumn": 30,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.check_crash",
          "line": 195,
          "column": 12,
          "endLine": 195,
          "endColumn": 18,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.check_crash",
          "line": 195,
          "column": 26,
          "endLine": 195,
          "endColumn": 32,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.check_crash",
          "line": 196,
          "column": 12,
          "endLine": 196,
          "endColumn": 18,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.check_crash",
          "line": 196,
          "column": 26,
          "endLine": 196,
          "endColumn": 32,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.check_crash",
          "line": 201,
          "column": 35,
          "endLine": 201,
          "endColumn": 41,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'x' member; maybe 'y'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "Snake.check_crash",
          "line": 201,
          "column": 57,
          "endLine": 201,
          "endColumn": 63,
          "path": "snake.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "snake",
          "obj": "Snake.init_body",
          "line": 84,
          "column": 8,
          "endLine": 84,
          "endColumn": 18,
          "path": "snake.py",
          "symbol": "attribute-defined-outside-init",
          "message": "Attribute 'score' defined outside __init__",
          "message-id": "W0201",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "snake",
          "obj": "Snake.init_body",
          "line": 85,
          "column": 8,
          "endLine": 85,
          "endColumn": 19,
          "path": "snake.py",
          "symbol": "attribute-defined-outside-init",
          "message": "Attribute 'length' defined outside __init__",
          "message-id": "W0201",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "snake",
          "obj": "Snake.add_score",
          "line": 150,
          "column": 12,
          "endLine": 150,
          "endColumn": 23,
          "path": "snake.py",
          "symbol": "attribute-defined-outside-init",
          "message": "Attribute 'length' defined outside __init__",
          "message-id": "W0201",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "snake",
          "obj": "Snake.init_body",
          "line": 86,
          "column": 8,
          "endLine": 86,
          "endColumn": 17,
          "path": "snake.py",
          "symbol": "attribute-defined-outside-init",
          "message": "Attribute 'body' defined outside __init__",
          "message-id": "W0201",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "snake",
          "obj": "",
          "line": 3,
          "column": 0,
          "endLine": 3,
          "endColumn": 10,
          "path": "snake.py",
          "symbol": "unused-import",
          "message": "Unused import sys",
          "message-id": "W0611",
          "tool": "pylint"
        },
        {
          "code": "41             enemy.optional_attr = enemy.nonexistent_attribute\n42         except:\n43             # swallow everything deliberately\n44             pass\n45 \n",
          "col_offset": 8,
          "end_col_offset": 16,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\arena.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 703,
            "link": "https://cwe.mitre.org/data/definitions/703.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Try, Except, Pass detected.",
          "line_number": 42,
          "line_range": [
            42,
            43,
            44
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b110_try_except_pass.html",
          "test_id": "B110",
          "test_name": "try_except_pass",
          "tool": "bandit"
        },
        {
          "code": "25         if color is None:\n26             color = random.choice(define.ALL_COLOR)\n27 \n",
          "col_offset": 20,
          "end_col_offset": 51,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 26,
          "line_range": [
            26
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "31         if pos is None:\n32             self.position = (random.randint(40, define.WIDTH - 40),\n33                              random.randint(40, define.HEIGHT - 40))\n",
          "col_offset": 29,
          "end_col_offset": 66,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 32,
          "line_range": [
            32
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "32             self.position = (random.randint(40, define.WIDTH - 40),\n33                              random.randint(40, define.HEIGHT - 40))\n34             self.is_big = False\n",
          "col_offset": 29,
          "end_col_offset": 67,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 33,
          "line_range": [
            33
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "36         else:\n37             self.position = (pos[0] + random.random() * 32 - 16,\n38                              pos[1] + random.random() * 32 - 16)\n",
          "col_offset": 38,
          "end_col_offset": 53,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 37,
          "line_range": [
            37
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "37             self.position = (pos[0] + random.random() * 32 - 16,\n38                              pos[1] + random.random() * 32 - 16)\n39             self.is_big = True\n",
          "col_offset": 38,
          "end_col_offset": 53,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 38,
          "line_range": [
            38
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "39             self.is_big = True\n40         self.schedule_interval(self.update, random.random() * 0.2 + 0.1)\n41 \n",
          "col_offset": 44,
          "end_col_offset": 59,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\dot.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 40,
          "line_range": [
            40
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "18         if isinstance(expr, str) and len(expr) < 50:\n19             return eval(expr)\n20     except Exception:\n",
          "col_offset": 19,
          "end_col_offset": 29,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 78,
            "link": "https://cwe.mitre.org/data/definitions/78.html"
          },
          "issue_severity": "MEDIUM",
          "issue_text": "Use of possibly insecure function - consider using safer ast.literal_eval.",
          "line_number": 19,
          "line_range": [
            19
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b307-eval",
          "test_id": "B307",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "28         # intentionally not closing here for detection exercises\n29     except Exception:\n30         pass\n31 \n",
          "col_offset": 4,
          "end_col_offset": 12,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\gluttonous.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 703,
            "link": "https://cwe.mitre.org/data/definitions/703.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Try, Except, Pass detected.",
          "line_number": 29,
          "line_range": [
            29,
            30
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b110_try_except_pass.html",
          "test_id": "B110",
          "test_name": "try_except_pass",
          "tool": "bandit"
        },
        {
          "code": "17         self.is_dead = False\n18         self.angle = random.randrange(360)  # 目前角度\n19         self.angle_dest = self.angle  # 目标角度\n",
          "col_offset": 21,
          "end_col_offset": 42,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 18,
          "line_range": [
            18
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "19         self.angle_dest = self.angle  # 目标角度\n20         self.color = random.choice(define.ALL_COLOR)\n21         self.no = Snake.no\n",
          "col_offset": 21,
          "end_col_offset": 52,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 20,
          "line_range": [
            20
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "23         if is_enemy:\n24             self.position = random.randrange(300, 1300), random.randrange(200, 600)\n25             if 600 < self.x < 1000:\n",
          "col_offset": 28,
          "end_col_offset": 55,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 24,
          "line_range": [
            24
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "23         if is_enemy:\n24             self.position = random.randrange(300, 1300), random.randrange(200, 600)\n25             if 600 < self.x < 1000:\n",
          "col_offset": 57,
          "end_col_offset": 83,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 24,
          "line_range": [
            24
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "27         else:\n28             self.position = random.randrange(700, 900), random.randrange(350, 450)\n29         self.is_enemy = is_enemy\n",
          "col_offset": 28,
          "end_col_offset": 54,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 28,
          "line_range": [
            28
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "27         else:\n28             self.position = random.randrange(700, 900), random.randrange(350, 450)\n29         self.is_enemy = is_enemy\n",
          "col_offset": 56,
          "end_col_offset": 82,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 28,
          "line_range": [
            28
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "56         if self.is_enemy:\n57             self.schedule_interval(self.ai, random.random() * 0.1 + 0.05)\n58 \n",
          "col_offset": 44,
          "end_col_offset": 59,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 57,
          "line_range": [
            57
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "78         Not called by default; present for dynamic detection exercises.\"\"\"\n79         import subprocess\n80         # benign command; uses shell=True to be flagged by scanners\n",
          "col_offset": 8,
          "end_col_offset": 25,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 78,
            "link": "https://cwe.mitre.org/data/definitions/78.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Consider possible security implications associated with the subprocess module.",
          "line_number": 79,
          "line_range": [
            79
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_imports.html#b404-import-subprocess",
          "test_id": "B404",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "80         # benign command; uses shell=True to be flagged by scanners\n81         subprocess.run(\"echo harmless\", shell=True)\n82 \n",
          "col_offset": 8,
          "end_col_offset": 51,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 78,
            "link": "https://cwe.mitre.org/data/definitions/78.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Starting a process with a partial executable path",
          "line_number": 81,
          "line_range": [
            81
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b607_start_process_with_partial_path.html",
          "test_id": "B607",
          "test_name": "start_process_with_partial_path",
          "tool": "bandit"
        },
        {
          "code": "80         # benign command; uses shell=True to be flagged by scanners\n81         subprocess.run(\"echo harmless\", shell=True)\n82 \n",
          "col_offset": 8,
          "end_col_offset": 51,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 78,
            "link": "https://cwe.mitre.org/data/definitions/78.html"
          },
          "issue_severity": "LOW",
          "issue_text": "subprocess call with shell=True seems safe, but may be changed in the future, consider rewriting without shell",
          "line_number": 81,
          "line_range": [
            81
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b602_subprocess_popen_with_shell_equals_true.html",
          "test_id": "B602",
          "test_name": "subprocess_popen_with_shell_equals_true",
          "tool": "bandit"
        },
        {
          "code": "189             if abs(angle - self.angle_dest) < 5:\n190                 self.angle_dest += random.randrange(90, 270)\n191 \n",
          "col_offset": 35,
          "end_col_offset": 60,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_zrtaug9o\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 190,
          "line_range": [
            190
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        }
      ],
      "dynamic_results": {
        "py_compile": [],
        "pytest": {
          "skipped": true,
          "reason": "未配置测试"
        }
      }
    }
  ]
}
```

## 🔧 修复详情（LLM 输出 + Diff）

### 📄 arena.py   （方法：llm，修复 0 处）
### 📄 dot.py   （方法：llm，修复 0 处）
### 📄 gameover.py   （方法：llm，修复 0 处）
### 📄 gluttonous.py   （方法：llm，修复 0 处）
### 📄 snake.py   （方法：llm，修复 0 处）
### 📄 define.py   （方法：llm，修复 0 处）
## 🧪 验证阶段

- ✅ arena.py 通过验证
- ✅ dot.py 通过验证
- ✅ gameover.py 通过验证
- ✅ gluttonous.py 通过验证
- ✅ snake.py 通过验证
- ✅ define.py 通过验证