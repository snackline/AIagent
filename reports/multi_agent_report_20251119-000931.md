# 🧾 Multi-Agent 详细修复报告

**生成时间**：2025-11-19 00:09:31.837174

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
    "total_issues": 105,
    "high_priority": 0,
    "medium_priority": 8,
    "low_priority": 97
  },
  "by_language": {
    "python": {
      "total": 105,
      "issues_by_file": {
        "arena.py": [
          {
            "file": "arena.py",
            "line": 13,
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
            "line": 40,
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
              "column": 27,
              "row": 7
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\arena.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import cocos\nfrom cocos import batch, layer\nfrom cocos.director import director\nfrom dot_sprite import Dot\n\nimport define\nfrom snake import Snake\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 9
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
            "code": "F401",
            "end_location": {
              "column": 13,
              "row": 1
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\arena.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "",
                  "end_location": {
                    "column": 1,
                    "row": 2
                  },
                  "location": {
                    "column": 1,
                    "row": 1
                  }
                }
              ],
              "message": "Remove unused import: `cocos`"
            },
            "location": {
              "column": 8,
              "row": 1
            },
            "message": "`cocos` imported but unused",
            "noqa_row": 1,
            "url": "https://docs.astral.sh/ruff/rules/unused-import",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E501",
            "end_location": {
              "column": 93,
              "row": 14
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\arena.py",
            "fix": null,
            "location": {
              "column": 89,
              "row": 14
            },
            "message": "Line too long (92 > 88)",
            "noqa_row": 14,
            "url": "https://docs.astral.sh/ruff/rules/line-too-long",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 51,
              "row": 53
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\arena.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 51,
                    "row": 53
                  },
                  "location": {
                    "column": 51,
                    "row": 53
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 51,
              "row": 53
            },
            "message": "No newline at end of file",
            "noqa_row": 53,
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
            "obj": "",
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 30,
            "path": "arena.py",
            "symbol": "no-name-in-module",
            "message": "No name 'layer' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "",
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 30,
            "path": "arena.py",
            "symbol": "no-name-in-module",
            "message": "No name 'batch' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "",
            "line": 7,
            "column": 0,
            "endLine": 7,
            "endColumn": 26,
            "path": "arena.py",
            "symbol": "import-error",
            "message": "Unable to import 'dot_sprite'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.add_enemy",
            "line": 40,
            "column": 15,
            "endLine": 40,
            "endColumn": 24,
            "path": "arena.py",
            "symbol": "broad-exception-caught",
            "message": "Catching too general exception Exception",
            "message-id": "W0718",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "Arena.update",
            "line": 44,
            "column": 34,
            "endLine": 44,
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
            "line": 45,
            "column": 34,
            "endLine": 45,
            "endColumn": 46,
            "path": "arena.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.update",
            "line": 43,
            "column": 21,
            "endLine": 43,
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
            "line": 47,
            "column": 32,
            "endLine": 47,
            "endColumn": 41,
            "path": "arena.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'modifiers'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.on_key_release",
            "line": 51,
            "column": 34,
            "endLine": 51,
            "endColumn": 43,
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
            "line": 44,
            "column": 8,
            "endLine": 44,
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
            "line": 45,
            "column": 8,
            "endLine": 45,
            "endColumn": 14,
            "path": "arena.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'y' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "",
            "line": 1,
            "column": 0,
            "endLine": 1,
            "endColumn": 12,
            "path": "arena.py",
            "symbol": "unused-import",
            "message": "Unused import cocos",
            "message-id": "W0611",
            "tool": "pylint"
          },
          {
            "code": "39             enemy.optional_attr = enemy.nonexistent_attribute\n40         except Exception:\n41             pass\n42 \n",
            "col_offset": 8,
            "end_col_offset": 16,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\arena.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 703,
              "link": "https://cwe.mitre.org/data/definitions/703.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Try, Except, Pass detected.",
            "line_number": 40,
            "line_range": [
              40,
              41
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
            "line": 12,
            "col": 24,
            "severity": "MEDIUM",
            "rule_id": "PY100",
            "message": "疑似使用了未定义的名称 'Dot'（可能为动态导入或第三方库）。  （合并 2 条相似问题）",
            "snippet": "        arena.batch.add(Dot())",
            "count": 2,
            "examples": [
              12,
              27
            ]
          },
          {
            "file": "dot.py",
            "line": 24,
            "col": 11,
            "severity": "MEDIUM",
            "rule_id": "AST002",
            "message": "疑似使用 'is' 进行值比较，建议使用 '==' （is 仅用于 None/True/False）。  （合并 2 条相似问题）",
            "snippet": "        if color is None:",
            "count": 2,
            "examples": [
              24,
              34
            ]
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 14,
              "row": 6
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import random\n\nfrom cocos.actions import CallFuncS, MoveTo\nfrom cocos.sprite import Sprite\n\nimport define\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 8
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
            "code": "W292",
            "end_location": {
              "column": 20,
              "row": 66
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 20,
                    "row": 66
                  },
                  "location": {
                    "column": 20,
                    "row": 66
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 20,
              "row": 66
            },
            "message": "No newline at end of file",
            "noqa_row": 66,
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
            "line": 45,
            "column": 21,
            "endLine": 45,
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
            "obj": "Dot.check_kill",
            "line": 57,
            "column": 12,
            "endLine": 57,
            "endColumn": 23,
            "path": "dot.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'killer' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "code": "24         if color is None:\n25             color = random.choice(define.ALL_COLOR)\n26 \n",
            "col_offset": 20,
            "end_col_offset": 51,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 25,
            "line_range": [
              25
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "34         if pos is None:\n35             self.position = (random.randint(40, define.WIDTH - 40),\n36                              random.randint(40, define.HEIGHT - 40))\n",
            "col_offset": 29,
            "end_col_offset": 66,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 35,
            "line_range": [
              35
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "35             self.position = (random.randint(40, define.WIDTH - 40),\n36                              random.randint(40, define.HEIGHT - 40))\n37             self.is_big = False\n",
            "col_offset": 29,
            "end_col_offset": 67,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 36,
            "line_range": [
              36
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "39         else:\n40             self.position = (pos[0] + random.random() * 32 - 16,\n41                              pos[1] + random.random() * 32 - 16)\n",
            "col_offset": 38,
            "end_col_offset": 53,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
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
            "code": "40             self.position = (pos[0] + random.random() * 32 - 16,\n41                              pos[1] + random.random() * 32 - 16)\n42             self.is_big = True\n",
            "col_offset": 38,
            "end_col_offset": 53,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 41,
            "line_range": [
              41
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "42             self.is_big = True\n43         self.schedule_interval(self.update, random.random() * 0.2 + 0.1)\n44 \n",
            "col_offset": 44,
            "end_col_offset": 59,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 43,
            "line_range": [
              43
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
            "line": 9,
            "col": 11,
            "severity": "MEDIUM",
            "rule_id": "AST002",
            "message": "疑似使用 'is' 进行值比较，建议使用 '==' （is 仅用于 None/True/False）。",
            "snippet": "        if banners is None:",
            "count": 1,
            "examples": []
          },
          {
            "file": "gameover.py",
            "line": 12,
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
              "row": 5
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\gameover.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import cocos\nfrom cocos import text\nfrom cocos.director import director\n\nimport define\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 7
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
            "code": "W292",
            "end_location": {
              "column": 29,
              "row": 35
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\gameover.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 29,
                    "row": 35
                  },
                  "location": {
                    "column": 29,
                    "row": 35
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 29,
              "row": 35
            },
            "message": "No newline at end of file",
            "noqa_row": 35,
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
            "obj": "",
            "line": 4,
            "column": 0,
            "endLine": 4,
            "endColumn": 22,
            "path": "gameover.py",
            "symbol": "no-name-in-module",
            "message": "No name 'text' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gameover",
            "obj": "Gameover",
            "line": 7,
            "column": 15,
            "endLine": 7,
            "endColumn": 26,
            "path": "gameover.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'layer' member",
            "message-id": "E1101",
            "tool": "pylint"
          }
        ],
        "gluttonous.py": [
          {
            "file": "gluttonous.py",
            "line": 14,
            "col": 8,
            "severity": "MEDIUM",
            "rule_id": "PY100",
            "message": "疑似使用了未定义的名称 'super'（可能为动态导入或第三方库）。",
            "snippet": "        super(HelloWorld, self).__init__()",
            "count": 1,
            "examples": []
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 30,
              "row": 8
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\gluttonous.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import cocos\nfrom cocos import layer, text\nfrom cocos.director import director\nfrom cocos.scene import Scene\n\nimport define\nfrom arena import Arena\nfrom gameover import Gameover\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 10
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
            "code": "F401",
            "end_location": {
              "column": 13,
              "row": 1
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\gluttonous.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "",
                  "end_location": {
                    "column": 1,
                    "row": 2
                  },
                  "location": {
                    "column": 1,
                    "row": 1
                  }
                }
              ],
              "message": "Remove unused import: `cocos`"
            },
            "location": {
              "column": 8,
              "row": 1
            },
            "message": "`cocos` imported but unused",
            "noqa_row": 1,
            "url": "https://docs.astral.sh/ruff/rules/unused-import",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 34,
              "row": 45
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\gluttonous.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 34,
                    "row": 45
                  },
                  "location": {
                    "column": 34,
                    "row": 45
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 34,
              "row": 45
            },
            "message": "No newline at end of file",
            "noqa_row": 45,
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
            "line": 2,
            "column": 0,
            "endLine": 2,
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
            "line": 3,
            "column": 0,
            "endLine": 3,
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
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 29,
            "path": "gluttonous.py",
            "symbol": "no-name-in-module",
            "message": "No name 'scene' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 4,
            "column": 0,
            "endLine": 4,
            "endColumn": 29,
            "path": "gluttonous.py",
            "symbol": "no-name-in-module",
            "message": "No name 'layer' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 4,
            "column": 0,
            "endLine": 4,
            "endColumn": 29,
            "path": "gluttonous.py",
            "symbol": "no-name-in-module",
            "message": "No name 'text' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "HelloWorld.on_mouse_press",
            "line": 35,
            "column": 29,
            "endLine": 35,
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
            "line": 35,
            "column": 32,
            "endLine": 35,
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
            "line": 35,
            "column": 35,
            "endLine": 35,
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
            "line": 35,
            "column": 44,
            "endLine": 35,
            "endColumn": 53,
            "path": "gluttonous.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'modifiers'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "",
            "line": 1,
            "column": 0,
            "endLine": 1,
            "endColumn": 12,
            "path": "gluttonous.py",
            "symbol": "unused-import",
            "message": "Unused import cocos",
            "message-id": "W0611",
            "tool": "pylint"
          }
        ],
        "snake.py": [
          {
            "file": "snake.py",
            "line": 14,
            "col": 8,
            "severity": "MEDIUM",
            "rule_id": "PY100",
            "message": "疑似使用了未定义的名称 'super'（可能为动态导入或第三方库）。  （合并 2 条相似问题）",
            "snippet": "        super(Snake, self).__init__()",
            "count": 2,
            "examples": [
              14,
              108
            ]
          },
          {
            "file": "snake.py",
            "line": 67,
            "col": 8,
            "severity": "LOW",
            "rule_id": "PY011",
            "message": "过于宽泛的异常捕获：Exception。  （合并 2 条相似问题）",
            "snippet": "        except Exception as e:",
            "count": 2,
            "examples": [
              67,
              204
            ]
          },
          {
            "file": "snake.py",
            "line": 130,
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
              "row": 8
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import math\nimport random\n\nimport cocos\nfrom cocos.sprite import Sprite\n\nimport define\nfrom dot import Dot\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 10
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
            "code": "B007",
            "end_location": {
              "column": 14,
              "row": 78
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "fix": {
              "applicability": "unsafe",
              "edits": [
                {
                  "content": "_i",
                  "end_location": {
                    "column": 14,
                    "row": 78
                  },
                  "location": {
                    "column": 13,
                    "row": 78
                  }
                }
              ],
              "message": "Rename unused `i` to `_i`"
            },
            "location": {
              "column": 13,
              "row": 78
            },
            "message": "Loop control variable `i` not used within loop body",
            "noqa_row": 78,
            "url": "https://docs.astral.sh/ruff/rules/unused-loop-control-variable",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E741",
            "end_location": {
              "column": 10,
              "row": 139
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "fix": null,
            "location": {
              "column": 9,
              "row": 139
            },
            "message": "Ambiguous variable name: `l`",
            "noqa_row": 139,
            "url": "https://docs.astral.sh/ruff/rules/ambiguous-variable-name",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 40,
              "row": 219
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 40,
                    "row": 219
                  },
                  "location": {
                    "column": 40,
                    "row": 219
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 40,
              "row": 219
            },
            "message": "No newline at end of file",
            "noqa_row": 219,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "",
            "line": 5,
            "column": 0,
            "endLine": 5,
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
            "line": 5,
            "column": 0,
            "endLine": 5,
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
            "line": 10,
            "column": 12,
            "endLine": 10,
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
            "line": 24,
            "column": 21,
            "endLine": 24,
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
            "line": 25,
            "column": 16,
            "endLine": 25,
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
            "line": 62,
            "column": 11,
            "endLine": 62,
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
            "line": 67,
            "column": 15,
            "endLine": 67,
            "endColumn": 24,
            "path": "snake.py",
            "symbol": "broad-exception-caught",
            "message": "Catching too general exception Exception",
            "message-id": "W0718",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.init_body",
            "line": 78,
            "column": 12,
            "endLine": 78,
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
            "line": 103,
            "column": 8,
            "endLine": 103,
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
            "line": 104,
            "column": 8,
            "endLine": 104,
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
            "line": 146,
            "column": 12,
            "endLine": 146,
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
            "line": 147,
            "column": 12,
            "endLine": 147,
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
            "line": 151,
            "column": 14,
            "endLine": 151,
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
            "line": 152,
            "column": 12,
            "endLine": 152,
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
            "line": 144,
            "column": 17,
            "endLine": 144,
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
            "line": 166,
            "column": 24,
            "endLine": 166,
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
            "line": 167,
            "column": 24,
            "endLine": 167,
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
            "line": 186,
            "column": 12,
            "endLine": 186,
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
            "line": 186,
            "column": 26,
            "endLine": 186,
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
            "line": 187,
            "column": 12,
            "endLine": 187,
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
            "line": 187,
            "column": 26,
            "endLine": 187,
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
            "line": 192,
            "column": 35,
            "endLine": 192,
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
            "line": 192,
            "column": 57,
            "endLine": 192,
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
            "obj": "Snake.crash",
            "line": 204,
            "column": 19,
            "endLine": 204,
            "endColumn": 28,
            "path": "snake.py",
            "symbol": "broad-exception-caught",
            "message": "Catching too general exception Exception",
            "message-id": "W0718",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.init_body",
            "line": 75,
            "column": 8,
            "endLine": 75,
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
            "line": 76,
            "column": 8,
            "endLine": 76,
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
            "line": 141,
            "column": 12,
            "endLine": 141,
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
            "line": 77,
            "column": 8,
            "endLine": 77,
            "endColumn": 17,
            "path": "snake.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'body' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "code": "15         self.is_dead = False\n16         self.angle = random.randrange(360)\n17         self.angle_dest = self.angle\n",
            "col_offset": 21,
            "end_col_offset": 42,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 16,
            "line_range": [
              16
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "18         # IndexError 检测\n19         self.color = random.choice(define.ALL_COLOR)\n20         self.no = Snake.no\n",
            "col_offset": 21,
            "end_col_offset": 52,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 19,
            "line_range": [
              19
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "22         if is_enemy:\n23             self.position = random.randrange(300, 1300), random.randrange(200, 600)\n24             if 600 < self.x < 1000:\n",
            "col_offset": 28,
            "end_col_offset": 55,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 23,
            "line_range": [
              23
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "22         if is_enemy:\n23             self.position = random.randrange(300, 1300), random.randrange(200, 600)\n24             if 600 < self.x < 1000:\n",
            "col_offset": 57,
            "end_col_offset": 83,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 23,
            "line_range": [
              23
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "26         else:\n27             self.position = random.randrange(700, 900), random.randrange(350, 450)\n28         self.is_enemy = is_enemy\n",
            "col_offset": 28,
            "end_col_offset": 54,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 27,
            "line_range": [
              27
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "26         else:\n27             self.position = random.randrange(700, 900), random.randrange(350, 450)\n28         self.is_enemy = is_enemy\n",
            "col_offset": 56,
            "end_col_offset": 82,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 27,
            "line_range": [
              27
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "55         if self.is_enemy:\n56             self.schedule_interval(self.ai, random.random() * 0.1 + 0.05)\n57 \n",
            "col_offset": 44,
            "end_col_offset": 59,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 56,
            "line_range": [
              56
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "180             if abs(angle - self.angle_dest) < 5:\n181                 self.angle_dest += random.randrange(90, 270)\n182 \n",
            "col_offset": 35,
            "end_col_offset": 60,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 181,
            "line_range": [
              181
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "203                 self.unschedul_ai()\n204             except Exception:\n205                 pass\n206             arena = self.parent\n",
            "col_offset": 12,
            "end_col_offset": 20,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 703,
              "link": "https://cwe.mitre.org/data/definitions/703.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Try, Except, Pass detected.",
            "line_number": 204,
            "line_range": [
              204,
              205
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b110_try_except_pass.html",
            "test_id": "B110",
            "test_name": "try_except_pass",
            "tool": "bandit"
          }
        ],
        "define.py": [
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 70,
              "row": 28
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\define.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 70,
                    "row": 28
                  },
                  "location": {
                    "column": 70,
                    "row": 28
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 70,
              "row": 28
            },
            "message": "No newline at end of file",
            "noqa_row": 28,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          }
        ]
      },
      "issues_by_severity": {
        "HIGH": [],
        "MEDIUM": [
          {
            "file": "arena.py",
            "line": 13,
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
            "line": 12,
            "col": 24,
            "severity": "MEDIUM",
            "rule_id": "PY100",
            "message": "疑似使用了未定义的名称 'Dot'（可能为动态导入或第三方库）。  （合并 2 条相似问题）",
            "snippet": "        arena.batch.add(Dot())",
            "count": 2,
            "examples": [
              12,
              27
            ]
          },
          {
            "file": "dot.py",
            "line": 24,
            "col": 11,
            "severity": "MEDIUM",
            "rule_id": "AST002",
            "message": "疑似使用 'is' 进行值比较，建议使用 '==' （is 仅用于 None/True/False）。  （合并 2 条相似问题）",
            "snippet": "        if color is None:",
            "count": 2,
            "examples": [
              24,
              34
            ]
          },
          {
            "file": "gameover.py",
            "line": 9,
            "col": 11,
            "severity": "MEDIUM",
            "rule_id": "AST002",
            "message": "疑似使用 'is' 进行值比较，建议使用 '==' （is 仅用于 None/True/False）。",
            "snippet": "        if banners is None:",
            "count": 1,
            "examples": []
          },
          {
            "file": "gameover.py",
            "line": 12,
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
            "line": 14,
            "col": 8,
            "severity": "MEDIUM",
            "rule_id": "PY100",
            "message": "疑似使用了未定义的名称 'super'（可能为动态导入或第三方库）。",
            "snippet": "        super(HelloWorld, self).__init__()",
            "count": 1,
            "examples": []
          },
          {
            "file": "snake.py",
            "line": 14,
            "col": 8,
            "severity": "MEDIUM",
            "rule_id": "PY100",
            "message": "疑似使用了未定义的名称 'super'（可能为动态导入或第三方库）。  （合并 2 条相似问题）",
            "snippet": "        super(Snake, self).__init__()",
            "count": 2,
            "examples": [
              14,
              108
            ]
          },
          {
            "file": "snake.py",
            "line": 130,
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
            "line": 40,
            "col": 8,
            "severity": "LOW",
            "rule_id": "PY011",
            "message": "过于宽泛的异常捕获：Exception。",
            "snippet": "        except Exception:",
            "count": 1,
            "examples": []
          },
          {
            "file": "snake.py",
            "line": 67,
            "col": 8,
            "severity": "LOW",
            "rule_id": "PY011",
            "message": "过于宽泛的异常捕获：Exception。  （合并 2 条相似问题）",
            "snippet": "        except Exception as e:",
            "count": 2,
            "examples": [
              67,
              204
            ]
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 27,
              "row": 7
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\arena.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import cocos\nfrom cocos import batch, layer\nfrom cocos.director import director\nfrom dot_sprite import Dot\n\nimport define\nfrom snake import Snake\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 9
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
            "code": "F401",
            "end_location": {
              "column": 13,
              "row": 1
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\arena.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "",
                  "end_location": {
                    "column": 1,
                    "row": 2
                  },
                  "location": {
                    "column": 1,
                    "row": 1
                  }
                }
              ],
              "message": "Remove unused import: `cocos`"
            },
            "location": {
              "column": 8,
              "row": 1
            },
            "message": "`cocos` imported but unused",
            "noqa_row": 1,
            "url": "https://docs.astral.sh/ruff/rules/unused-import",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E501",
            "end_location": {
              "column": 93,
              "row": 14
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\arena.py",
            "fix": null,
            "location": {
              "column": 89,
              "row": 14
            },
            "message": "Line too long (92 > 88)",
            "noqa_row": 14,
            "url": "https://docs.astral.sh/ruff/rules/line-too-long",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 51,
              "row": 53
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\arena.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 51,
                    "row": 53
                  },
                  "location": {
                    "column": 51,
                    "row": 53
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 51,
              "row": 53
            },
            "message": "No newline at end of file",
            "noqa_row": 53,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 70,
              "row": 28
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\define.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 70,
                    "row": 28
                  },
                  "location": {
                    "column": 70,
                    "row": 28
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 70,
              "row": 28
            },
            "message": "No newline at end of file",
            "noqa_row": 28,
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
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import random\n\nfrom cocos.actions import CallFuncS, MoveTo\nfrom cocos.sprite import Sprite\n\nimport define\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 8
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
            "code": "W292",
            "end_location": {
              "column": 20,
              "row": 66
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 20,
                    "row": 66
                  },
                  "location": {
                    "column": 20,
                    "row": 66
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 20,
              "row": 66
            },
            "message": "No newline at end of file",
            "noqa_row": 66,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 14,
              "row": 5
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\gameover.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import cocos\nfrom cocos import text\nfrom cocos.director import director\n\nimport define\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 7
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
            "code": "W292",
            "end_location": {
              "column": 29,
              "row": 35
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\gameover.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 29,
                    "row": 35
                  },
                  "location": {
                    "column": 29,
                    "row": 35
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 29,
              "row": 35
            },
            "message": "No newline at end of file",
            "noqa_row": 35,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 30,
              "row": 8
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\gluttonous.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import cocos\nfrom cocos import layer, text\nfrom cocos.director import director\nfrom cocos.scene import Scene\n\nimport define\nfrom arena import Arena\nfrom gameover import Gameover\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 10
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
            "code": "F401",
            "end_location": {
              "column": 13,
              "row": 1
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\gluttonous.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "",
                  "end_location": {
                    "column": 1,
                    "row": 2
                  },
                  "location": {
                    "column": 1,
                    "row": 1
                  }
                }
              ],
              "message": "Remove unused import: `cocos`"
            },
            "location": {
              "column": 8,
              "row": 1
            },
            "message": "`cocos` imported but unused",
            "noqa_row": 1,
            "url": "https://docs.astral.sh/ruff/rules/unused-import",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 34,
              "row": 45
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\gluttonous.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 34,
                    "row": 45
                  },
                  "location": {
                    "column": 34,
                    "row": 45
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 34,
              "row": 45
            },
            "message": "No newline at end of file",
            "noqa_row": 45,
            "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "I001",
            "end_location": {
              "column": 20,
              "row": 8
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "import math\nimport random\n\nimport cocos\nfrom cocos.sprite import Sprite\n\nimport define\nfrom dot import Dot\n\n\n",
                  "end_location": {
                    "column": 1,
                    "row": 10
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
            "code": "B007",
            "end_location": {
              "column": 14,
              "row": 78
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "fix": {
              "applicability": "unsafe",
              "edits": [
                {
                  "content": "_i",
                  "end_location": {
                    "column": 14,
                    "row": 78
                  },
                  "location": {
                    "column": 13,
                    "row": 78
                  }
                }
              ],
              "message": "Rename unused `i` to `_i`"
            },
            "location": {
              "column": 13,
              "row": 78
            },
            "message": "Loop control variable `i` not used within loop body",
            "noqa_row": 78,
            "url": "https://docs.astral.sh/ruff/rules/unused-loop-control-variable",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "E741",
            "end_location": {
              "column": 10,
              "row": 139
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "fix": null,
            "location": {
              "column": 9,
              "row": 139
            },
            "message": "Ambiguous variable name: `l`",
            "noqa_row": 139,
            "url": "https://docs.astral.sh/ruff/rules/ambiguous-variable-name",
            "tool": "ruff"
          },
          {
            "cell": null,
            "code": "W292",
            "end_location": {
              "column": 40,
              "row": 219
            },
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "fix": {
              "applicability": "safe",
              "edits": [
                {
                  "content": "\n",
                  "end_location": {
                    "column": 40,
                    "row": 219
                  },
                  "location": {
                    "column": 40,
                    "row": 219
                  }
                }
              ],
              "message": "Add trailing newline"
            },
            "location": {
              "column": 40,
              "row": 219
            },
            "message": "No newline at end of file",
            "noqa_row": 219,
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
            "obj": "",
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 30,
            "path": "arena.py",
            "symbol": "no-name-in-module",
            "message": "No name 'layer' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "",
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 30,
            "path": "arena.py",
            "symbol": "no-name-in-module",
            "message": "No name 'batch' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "",
            "line": 7,
            "column": 0,
            "endLine": 7,
            "endColumn": 26,
            "path": "arena.py",
            "symbol": "import-error",
            "message": "Unable to import 'dot_sprite'",
            "message-id": "E0401",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.add_enemy",
            "line": 40,
            "column": 15,
            "endLine": 40,
            "endColumn": 24,
            "path": "arena.py",
            "symbol": "broad-exception-caught",
            "message": "Catching too general exception Exception",
            "message-id": "W0718",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "arena",
            "obj": "Arena.update",
            "line": 44,
            "column": 34,
            "endLine": 44,
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
            "line": 45,
            "column": 34,
            "endLine": 45,
            "endColumn": 46,
            "path": "arena.py",
            "symbol": "no-member",
            "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
            "message-id": "E1101",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.update",
            "line": 43,
            "column": 21,
            "endLine": 43,
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
            "line": 47,
            "column": 32,
            "endLine": 47,
            "endColumn": 41,
            "path": "arena.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'modifiers'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "Arena.on_key_release",
            "line": 51,
            "column": 34,
            "endLine": 51,
            "endColumn": 43,
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
            "line": 44,
            "column": 8,
            "endLine": 44,
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
            "line": 45,
            "column": 8,
            "endLine": 45,
            "endColumn": 14,
            "path": "arena.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'y' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "arena",
            "obj": "",
            "line": 1,
            "column": 0,
            "endLine": 1,
            "endColumn": 12,
            "path": "arena.py",
            "symbol": "unused-import",
            "message": "Unused import cocos",
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
            "line": 45,
            "column": 21,
            "endLine": 45,
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
            "obj": "Dot.check_kill",
            "line": 57,
            "column": 12,
            "endLine": 57,
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
            "obj": "",
            "line": 4,
            "column": 0,
            "endLine": 4,
            "endColumn": 22,
            "path": "gameover.py",
            "symbol": "no-name-in-module",
            "message": "No name 'text' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gameover",
            "obj": "Gameover",
            "line": 7,
            "column": 15,
            "endLine": 7,
            "endColumn": 26,
            "path": "gameover.py",
            "symbol": "no-member",
            "message": "Module 'cocos' has no 'layer' member",
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
            "line": 2,
            "column": 0,
            "endLine": 2,
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
            "line": 3,
            "column": 0,
            "endLine": 3,
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
            "line": 3,
            "column": 0,
            "endLine": 3,
            "endColumn": 29,
            "path": "gluttonous.py",
            "symbol": "no-name-in-module",
            "message": "No name 'scene' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 4,
            "column": 0,
            "endLine": 4,
            "endColumn": 29,
            "path": "gluttonous.py",
            "symbol": "no-name-in-module",
            "message": "No name 'layer' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "gluttonous",
            "obj": "",
            "line": 4,
            "column": 0,
            "endLine": 4,
            "endColumn": 29,
            "path": "gluttonous.py",
            "symbol": "no-name-in-module",
            "message": "No name 'text' in module 'cocos'",
            "message-id": "E0611",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "HelloWorld.on_mouse_press",
            "line": 35,
            "column": 29,
            "endLine": 35,
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
            "line": 35,
            "column": 32,
            "endLine": 35,
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
            "line": 35,
            "column": 35,
            "endLine": 35,
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
            "line": 35,
            "column": 44,
            "endLine": 35,
            "endColumn": 53,
            "path": "gluttonous.py",
            "symbol": "unused-argument",
            "message": "Unused argument 'modifiers'",
            "message-id": "W0613",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "gluttonous",
            "obj": "",
            "line": 1,
            "column": 0,
            "endLine": 1,
            "endColumn": 12,
            "path": "gluttonous.py",
            "symbol": "unused-import",
            "message": "Unused import cocos",
            "message-id": "W0611",
            "tool": "pylint"
          },
          {
            "type": "error",
            "module": "snake",
            "obj": "",
            "line": 5,
            "column": 0,
            "endLine": 5,
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
            "line": 5,
            "column": 0,
            "endLine": 5,
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
            "line": 10,
            "column": 12,
            "endLine": 10,
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
            "line": 24,
            "column": 21,
            "endLine": 24,
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
            "line": 25,
            "column": 16,
            "endLine": 25,
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
            "line": 62,
            "column": 11,
            "endLine": 62,
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
            "line": 67,
            "column": 15,
            "endLine": 67,
            "endColumn": 24,
            "path": "snake.py",
            "symbol": "broad-exception-caught",
            "message": "Catching too general exception Exception",
            "message-id": "W0718",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.init_body",
            "line": 78,
            "column": 12,
            "endLine": 78,
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
            "line": 103,
            "column": 8,
            "endLine": 103,
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
            "line": 104,
            "column": 8,
            "endLine": 104,
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
            "line": 146,
            "column": 12,
            "endLine": 146,
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
            "line": 147,
            "column": 12,
            "endLine": 147,
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
            "line": 151,
            "column": 14,
            "endLine": 151,
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
            "line": 152,
            "column": 12,
            "endLine": 152,
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
            "line": 144,
            "column": 17,
            "endLine": 144,
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
            "line": 166,
            "column": 24,
            "endLine": 166,
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
            "line": 167,
            "column": 24,
            "endLine": 167,
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
            "line": 186,
            "column": 12,
            "endLine": 186,
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
            "line": 186,
            "column": 26,
            "endLine": 186,
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
            "line": 187,
            "column": 12,
            "endLine": 187,
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
            "line": 187,
            "column": 26,
            "endLine": 187,
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
            "line": 192,
            "column": 35,
            "endLine": 192,
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
            "line": 192,
            "column": 57,
            "endLine": 192,
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
            "obj": "Snake.crash",
            "line": 204,
            "column": 19,
            "endLine": 204,
            "endColumn": 28,
            "path": "snake.py",
            "symbol": "broad-exception-caught",
            "message": "Catching too general exception Exception",
            "message-id": "W0718",
            "tool": "pylint"
          },
          {
            "type": "warning",
            "module": "snake",
            "obj": "Snake.init_body",
            "line": 75,
            "column": 8,
            "endLine": 75,
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
            "line": 76,
            "column": 8,
            "endLine": 76,
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
            "line": 141,
            "column": 12,
            "endLine": 141,
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
            "line": 77,
            "column": 8,
            "endLine": 77,
            "endColumn": 17,
            "path": "snake.py",
            "symbol": "attribute-defined-outside-init",
            "message": "Attribute 'body' defined outside __init__",
            "message-id": "W0201",
            "tool": "pylint"
          },
          {
            "code": "39             enemy.optional_attr = enemy.nonexistent_attribute\n40         except Exception:\n41             pass\n42 \n",
            "col_offset": 8,
            "end_col_offset": 16,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\arena.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 703,
              "link": "https://cwe.mitre.org/data/definitions/703.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Try, Except, Pass detected.",
            "line_number": 40,
            "line_range": [
              40,
              41
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b110_try_except_pass.html",
            "test_id": "B110",
            "test_name": "try_except_pass",
            "tool": "bandit"
          },
          {
            "code": "24         if color is None:\n25             color = random.choice(define.ALL_COLOR)\n26 \n",
            "col_offset": 20,
            "end_col_offset": 51,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 25,
            "line_range": [
              25
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "34         if pos is None:\n35             self.position = (random.randint(40, define.WIDTH - 40),\n36                              random.randint(40, define.HEIGHT - 40))\n",
            "col_offset": 29,
            "end_col_offset": 66,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 35,
            "line_range": [
              35
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "35             self.position = (random.randint(40, define.WIDTH - 40),\n36                              random.randint(40, define.HEIGHT - 40))\n37             self.is_big = False\n",
            "col_offset": 29,
            "end_col_offset": 67,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 36,
            "line_range": [
              36
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "39         else:\n40             self.position = (pos[0] + random.random() * 32 - 16,\n41                              pos[1] + random.random() * 32 - 16)\n",
            "col_offset": 38,
            "end_col_offset": 53,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
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
            "code": "40             self.position = (pos[0] + random.random() * 32 - 16,\n41                              pos[1] + random.random() * 32 - 16)\n42             self.is_big = True\n",
            "col_offset": 38,
            "end_col_offset": 53,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 41,
            "line_range": [
              41
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "42             self.is_big = True\n43         self.schedule_interval(self.update, random.random() * 0.2 + 0.1)\n44 \n",
            "col_offset": 44,
            "end_col_offset": 59,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 43,
            "line_range": [
              43
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "15         self.is_dead = False\n16         self.angle = random.randrange(360)\n17         self.angle_dest = self.angle\n",
            "col_offset": 21,
            "end_col_offset": 42,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 16,
            "line_range": [
              16
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "18         # IndexError 检测\n19         self.color = random.choice(define.ALL_COLOR)\n20         self.no = Snake.no\n",
            "col_offset": 21,
            "end_col_offset": 52,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 19,
            "line_range": [
              19
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "22         if is_enemy:\n23             self.position = random.randrange(300, 1300), random.randrange(200, 600)\n24             if 600 < self.x < 1000:\n",
            "col_offset": 28,
            "end_col_offset": 55,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 23,
            "line_range": [
              23
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "22         if is_enemy:\n23             self.position = random.randrange(300, 1300), random.randrange(200, 600)\n24             if 600 < self.x < 1000:\n",
            "col_offset": 57,
            "end_col_offset": 83,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 23,
            "line_range": [
              23
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "26         else:\n27             self.position = random.randrange(700, 900), random.randrange(350, 450)\n28         self.is_enemy = is_enemy\n",
            "col_offset": 28,
            "end_col_offset": 54,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 27,
            "line_range": [
              27
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "26         else:\n27             self.position = random.randrange(700, 900), random.randrange(350, 450)\n28         self.is_enemy = is_enemy\n",
            "col_offset": 56,
            "end_col_offset": 82,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 27,
            "line_range": [
              27
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "55         if self.is_enemy:\n56             self.schedule_interval(self.ai, random.random() * 0.1 + 0.05)\n57 \n",
            "col_offset": 44,
            "end_col_offset": 59,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 56,
            "line_range": [
              56
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "180             if abs(angle - self.angle_dest) < 5:\n181                 self.angle_dest += random.randrange(90, 270)\n182 \n",
            "col_offset": 35,
            "end_col_offset": 60,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 330,
              "link": "https://cwe.mitre.org/data/definitions/330.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 181,
            "line_range": [
              181
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
            "test_id": "B311",
            "test_name": "blacklist",
            "tool": "bandit"
          },
          {
            "code": "203                 self.unschedul_ai()\n204             except Exception:\n205                 pass\n206             arena = self.parent\n",
            "col_offset": 12,
            "end_col_offset": 20,
            "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {
              "id": 703,
              "link": "https://cwe.mitre.org/data/definitions/703.html"
            },
            "issue_severity": "LOW",
            "issue_text": "Try, Except, Pass detected.",
            "line_number": 204,
            "line_range": [
              204,
              205
            ],
            "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b110_try_except_pass.html",
            "test_id": "B110",
            "test_name": "try_except_pass",
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
  "recommendations": [],
  "fix_plans": [
    {
      "language": "python",
      "total_issues": 105,
      "high": 0,
      "medium": 8,
      "low": 97,
      "priority_score": 137,
      "builtin_issues": [
        {
          "file": "arena.py",
          "line": 13,
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
          "line": 40,
          "col": 8,
          "severity": "LOW",
          "rule_id": "PY011",
          "message": "过于宽泛的异常捕获：Exception。",
          "snippet": "        except Exception:",
          "count": 1,
          "examples": []
        },
        {
          "file": "dot.py",
          "line": 12,
          "col": 24,
          "severity": "MEDIUM",
          "rule_id": "PY100",
          "message": "疑似使用了未定义的名称 'Dot'（可能为动态导入或第三方库）。  （合并 2 条相似问题）",
          "snippet": "        arena.batch.add(Dot())",
          "count": 2,
          "examples": [
            12,
            27
          ]
        },
        {
          "file": "dot.py",
          "line": 24,
          "col": 11,
          "severity": "MEDIUM",
          "rule_id": "AST002",
          "message": "疑似使用 'is' 进行值比较，建议使用 '==' （is 仅用于 None/True/False）。  （合并 2 条相似问题）",
          "snippet": "        if color is None:",
          "count": 2,
          "examples": [
            24,
            34
          ]
        },
        {
          "file": "gameover.py",
          "line": 9,
          "col": 11,
          "severity": "MEDIUM",
          "rule_id": "AST002",
          "message": "疑似使用 'is' 进行值比较，建议使用 '==' （is 仅用于 None/True/False）。",
          "snippet": "        if banners is None:",
          "count": 1,
          "examples": []
        },
        {
          "file": "gameover.py",
          "line": 12,
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
          "line": 14,
          "col": 8,
          "severity": "MEDIUM",
          "rule_id": "PY100",
          "message": "疑似使用了未定义的名称 'super'（可能为动态导入或第三方库）。",
          "snippet": "        super(HelloWorld, self).__init__()",
          "count": 1,
          "examples": []
        },
        {
          "file": "snake.py",
          "line": 14,
          "col": 8,
          "severity": "MEDIUM",
          "rule_id": "PY100",
          "message": "疑似使用了未定义的名称 'super'（可能为动态导入或第三方库）。  （合并 2 条相似问题）",
          "snippet": "        super(Snake, self).__init__()",
          "count": 2,
          "examples": [
            14,
            108
          ]
        },
        {
          "file": "snake.py",
          "line": 67,
          "col": 8,
          "severity": "LOW",
          "rule_id": "PY011",
          "message": "过于宽泛的异常捕获：Exception。  （合并 2 条相似问题）",
          "snippet": "        except Exception as e:",
          "count": 2,
          "examples": [
            67,
            204
          ]
        },
        {
          "file": "snake.py",
          "line": 130,
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
            "column": 27,
            "row": 7
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\arena.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "import cocos\nfrom cocos import batch, layer\nfrom cocos.director import director\nfrom dot_sprite import Dot\n\nimport define\nfrom snake import Snake\n\n\n",
                "end_location": {
                  "column": 1,
                  "row": 9
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
          "code": "F401",
          "end_location": {
            "column": 13,
            "row": 1
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\arena.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "",
                "end_location": {
                  "column": 1,
                  "row": 2
                },
                "location": {
                  "column": 1,
                  "row": 1
                }
              }
            ],
            "message": "Remove unused import: `cocos`"
          },
          "location": {
            "column": 8,
            "row": 1
          },
          "message": "`cocos` imported but unused",
          "noqa_row": 1,
          "url": "https://docs.astral.sh/ruff/rules/unused-import",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "E501",
          "end_location": {
            "column": 93,
            "row": 14
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\arena.py",
          "fix": null,
          "location": {
            "column": 89,
            "row": 14
          },
          "message": "Line too long (92 > 88)",
          "noqa_row": 14,
          "url": "https://docs.astral.sh/ruff/rules/line-too-long",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "W292",
          "end_location": {
            "column": 51,
            "row": 53
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\arena.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "\n",
                "end_location": {
                  "column": 51,
                  "row": 53
                },
                "location": {
                  "column": 51,
                  "row": 53
                }
              }
            ],
            "message": "Add trailing newline"
          },
          "location": {
            "column": 51,
            "row": 53
          },
          "message": "No newline at end of file",
          "noqa_row": 53,
          "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "W292",
          "end_location": {
            "column": 70,
            "row": 28
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\define.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "\n",
                "end_location": {
                  "column": 70,
                  "row": 28
                },
                "location": {
                  "column": 70,
                  "row": 28
                }
              }
            ],
            "message": "Add trailing newline"
          },
          "location": {
            "column": 70,
            "row": 28
          },
          "message": "No newline at end of file",
          "noqa_row": 28,
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
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "import random\n\nfrom cocos.actions import CallFuncS, MoveTo\nfrom cocos.sprite import Sprite\n\nimport define\n\n\n",
                "end_location": {
                  "column": 1,
                  "row": 8
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
          "code": "W292",
          "end_location": {
            "column": 20,
            "row": 66
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "\n",
                "end_location": {
                  "column": 20,
                  "row": 66
                },
                "location": {
                  "column": 20,
                  "row": 66
                }
              }
            ],
            "message": "Add trailing newline"
          },
          "location": {
            "column": 20,
            "row": 66
          },
          "message": "No newline at end of file",
          "noqa_row": 66,
          "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "I001",
          "end_location": {
            "column": 14,
            "row": 5
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\gameover.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "import cocos\nfrom cocos import text\nfrom cocos.director import director\n\nimport define\n\n\n",
                "end_location": {
                  "column": 1,
                  "row": 7
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
          "code": "W292",
          "end_location": {
            "column": 29,
            "row": 35
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\gameover.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "\n",
                "end_location": {
                  "column": 29,
                  "row": 35
                },
                "location": {
                  "column": 29,
                  "row": 35
                }
              }
            ],
            "message": "Add trailing newline"
          },
          "location": {
            "column": 29,
            "row": 35
          },
          "message": "No newline at end of file",
          "noqa_row": 35,
          "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "I001",
          "end_location": {
            "column": 30,
            "row": 8
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\gluttonous.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "import cocos\nfrom cocos import layer, text\nfrom cocos.director import director\nfrom cocos.scene import Scene\n\nimport define\nfrom arena import Arena\nfrom gameover import Gameover\n\n\n",
                "end_location": {
                  "column": 1,
                  "row": 10
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
          "code": "F401",
          "end_location": {
            "column": 13,
            "row": 1
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\gluttonous.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "",
                "end_location": {
                  "column": 1,
                  "row": 2
                },
                "location": {
                  "column": 1,
                  "row": 1
                }
              }
            ],
            "message": "Remove unused import: `cocos`"
          },
          "location": {
            "column": 8,
            "row": 1
          },
          "message": "`cocos` imported but unused",
          "noqa_row": 1,
          "url": "https://docs.astral.sh/ruff/rules/unused-import",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "W292",
          "end_location": {
            "column": 34,
            "row": 45
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\gluttonous.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "\n",
                "end_location": {
                  "column": 34,
                  "row": 45
                },
                "location": {
                  "column": 34,
                  "row": 45
                }
              }
            ],
            "message": "Add trailing newline"
          },
          "location": {
            "column": 34,
            "row": 45
          },
          "message": "No newline at end of file",
          "noqa_row": 45,
          "url": "https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "I001",
          "end_location": {
            "column": 20,
            "row": 8
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "import math\nimport random\n\nimport cocos\nfrom cocos.sprite import Sprite\n\nimport define\nfrom dot import Dot\n\n\n",
                "end_location": {
                  "column": 1,
                  "row": 10
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
          "code": "B007",
          "end_location": {
            "column": 14,
            "row": 78
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
          "fix": {
            "applicability": "unsafe",
            "edits": [
              {
                "content": "_i",
                "end_location": {
                  "column": 14,
                  "row": 78
                },
                "location": {
                  "column": 13,
                  "row": 78
                }
              }
            ],
            "message": "Rename unused `i` to `_i`"
          },
          "location": {
            "column": 13,
            "row": 78
          },
          "message": "Loop control variable `i` not used within loop body",
          "noqa_row": 78,
          "url": "https://docs.astral.sh/ruff/rules/unused-loop-control-variable",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "E741",
          "end_location": {
            "column": 10,
            "row": 139
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
          "fix": null,
          "location": {
            "column": 9,
            "row": 139
          },
          "message": "Ambiguous variable name: `l`",
          "noqa_row": 139,
          "url": "https://docs.astral.sh/ruff/rules/ambiguous-variable-name",
          "tool": "ruff"
        },
        {
          "cell": null,
          "code": "W292",
          "end_location": {
            "column": 40,
            "row": 219
          },
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
          "fix": {
            "applicability": "safe",
            "edits": [
              {
                "content": "\n",
                "end_location": {
                  "column": 40,
                  "row": 219
                },
                "location": {
                  "column": 40,
                  "row": 219
                }
              }
            ],
            "message": "Add trailing newline"
          },
          "location": {
            "column": 40,
            "row": 219
          },
          "message": "No newline at end of file",
          "noqa_row": 219,
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
          "obj": "",
          "line": 3,
          "column": 0,
          "endLine": 3,
          "endColumn": 30,
          "path": "arena.py",
          "symbol": "no-name-in-module",
          "message": "No name 'layer' in module 'cocos'",
          "message-id": "E0611",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "arena",
          "obj": "",
          "line": 3,
          "column": 0,
          "endLine": 3,
          "endColumn": 30,
          "path": "arena.py",
          "symbol": "no-name-in-module",
          "message": "No name 'batch' in module 'cocos'",
          "message-id": "E0611",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "arena",
          "obj": "",
          "line": 7,
          "column": 0,
          "endLine": 7,
          "endColumn": 26,
          "path": "arena.py",
          "symbol": "import-error",
          "message": "Unable to import 'dot_sprite'",
          "message-id": "E0401",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "arena",
          "obj": "Arena.add_enemy",
          "line": 40,
          "column": 15,
          "endLine": 40,
          "endColumn": 24,
          "path": "arena.py",
          "symbol": "broad-exception-caught",
          "message": "Catching too general exception Exception",
          "message-id": "W0718",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "arena",
          "obj": "Arena.update",
          "line": 44,
          "column": 34,
          "endLine": 44,
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
          "line": 45,
          "column": 34,
          "endLine": 45,
          "endColumn": 46,
          "path": "arena.py",
          "symbol": "no-member",
          "message": "Instance of 'Snake' has no 'y' member; maybe 'x'?",
          "message-id": "E1101",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "arena",
          "obj": "Arena.update",
          "line": 43,
          "column": 21,
          "endLine": 43,
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
          "line": 47,
          "column": 32,
          "endLine": 47,
          "endColumn": 41,
          "path": "arena.py",
          "symbol": "unused-argument",
          "message": "Unused argument 'modifiers'",
          "message-id": "W0613",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "arena",
          "obj": "Arena.on_key_release",
          "line": 51,
          "column": 34,
          "endLine": 51,
          "endColumn": 43,
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
          "line": 44,
          "column": 8,
          "endLine": 44,
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
          "line": 45,
          "column": 8,
          "endLine": 45,
          "endColumn": 14,
          "path": "arena.py",
          "symbol": "attribute-defined-outside-init",
          "message": "Attribute 'y' defined outside __init__",
          "message-id": "W0201",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "arena",
          "obj": "",
          "line": 1,
          "column": 0,
          "endLine": 1,
          "endColumn": 12,
          "path": "arena.py",
          "symbol": "unused-import",
          "message": "Unused import cocos",
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
          "line": 45,
          "column": 21,
          "endLine": 45,
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
          "obj": "Dot.check_kill",
          "line": 57,
          "column": 12,
          "endLine": 57,
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
          "obj": "",
          "line": 4,
          "column": 0,
          "endLine": 4,
          "endColumn": 22,
          "path": "gameover.py",
          "symbol": "no-name-in-module",
          "message": "No name 'text' in module 'cocos'",
          "message-id": "E0611",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gameover",
          "obj": "Gameover",
          "line": 7,
          "column": 15,
          "endLine": 7,
          "endColumn": 26,
          "path": "gameover.py",
          "symbol": "no-member",
          "message": "Module 'cocos' has no 'layer' member",
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
          "line": 2,
          "column": 0,
          "endLine": 2,
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
          "line": 3,
          "column": 0,
          "endLine": 3,
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
          "line": 3,
          "column": 0,
          "endLine": 3,
          "endColumn": 29,
          "path": "gluttonous.py",
          "symbol": "no-name-in-module",
          "message": "No name 'scene' in module 'cocos'",
          "message-id": "E0611",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gluttonous",
          "obj": "",
          "line": 4,
          "column": 0,
          "endLine": 4,
          "endColumn": 29,
          "path": "gluttonous.py",
          "symbol": "no-name-in-module",
          "message": "No name 'layer' in module 'cocos'",
          "message-id": "E0611",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "gluttonous",
          "obj": "",
          "line": 4,
          "column": 0,
          "endLine": 4,
          "endColumn": 29,
          "path": "gluttonous.py",
          "symbol": "no-name-in-module",
          "message": "No name 'text' in module 'cocos'",
          "message-id": "E0611",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "gluttonous",
          "obj": "HelloWorld.on_mouse_press",
          "line": 35,
          "column": 29,
          "endLine": 35,
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
          "line": 35,
          "column": 32,
          "endLine": 35,
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
          "line": 35,
          "column": 35,
          "endLine": 35,
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
          "line": 35,
          "column": 44,
          "endLine": 35,
          "endColumn": 53,
          "path": "gluttonous.py",
          "symbol": "unused-argument",
          "message": "Unused argument 'modifiers'",
          "message-id": "W0613",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "gluttonous",
          "obj": "",
          "line": 1,
          "column": 0,
          "endLine": 1,
          "endColumn": 12,
          "path": "gluttonous.py",
          "symbol": "unused-import",
          "message": "Unused import cocos",
          "message-id": "W0611",
          "tool": "pylint"
        },
        {
          "type": "error",
          "module": "snake",
          "obj": "",
          "line": 5,
          "column": 0,
          "endLine": 5,
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
          "line": 5,
          "column": 0,
          "endLine": 5,
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
          "line": 10,
          "column": 12,
          "endLine": 10,
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
          "line": 24,
          "column": 21,
          "endLine": 24,
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
          "line": 25,
          "column": 16,
          "endLine": 25,
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
          "line": 62,
          "column": 11,
          "endLine": 62,
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
          "line": 67,
          "column": 15,
          "endLine": 67,
          "endColumn": 24,
          "path": "snake.py",
          "symbol": "broad-exception-caught",
          "message": "Catching too general exception Exception",
          "message-id": "W0718",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "snake",
          "obj": "Snake.init_body",
          "line": 78,
          "column": 12,
          "endLine": 78,
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
          "line": 103,
          "column": 8,
          "endLine": 103,
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
          "line": 104,
          "column": 8,
          "endLine": 104,
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
          "line": 146,
          "column": 12,
          "endLine": 146,
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
          "line": 147,
          "column": 12,
          "endLine": 147,
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
          "line": 151,
          "column": 14,
          "endLine": 151,
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
          "line": 152,
          "column": 12,
          "endLine": 152,
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
          "line": 144,
          "column": 17,
          "endLine": 144,
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
          "line": 166,
          "column": 24,
          "endLine": 166,
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
          "line": 167,
          "column": 24,
          "endLine": 167,
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
          "line": 186,
          "column": 12,
          "endLine": 186,
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
          "line": 186,
          "column": 26,
          "endLine": 186,
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
          "line": 187,
          "column": 12,
          "endLine": 187,
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
          "line": 187,
          "column": 26,
          "endLine": 187,
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
          "line": 192,
          "column": 35,
          "endLine": 192,
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
          "line": 192,
          "column": 57,
          "endLine": 192,
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
          "obj": "Snake.crash",
          "line": 204,
          "column": 19,
          "endLine": 204,
          "endColumn": 28,
          "path": "snake.py",
          "symbol": "broad-exception-caught",
          "message": "Catching too general exception Exception",
          "message-id": "W0718",
          "tool": "pylint"
        },
        {
          "type": "warning",
          "module": "snake",
          "obj": "Snake.init_body",
          "line": 75,
          "column": 8,
          "endLine": 75,
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
          "line": 76,
          "column": 8,
          "endLine": 76,
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
          "line": 141,
          "column": 12,
          "endLine": 141,
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
          "line": 77,
          "column": 8,
          "endLine": 77,
          "endColumn": 17,
          "path": "snake.py",
          "symbol": "attribute-defined-outside-init",
          "message": "Attribute 'body' defined outside __init__",
          "message-id": "W0201",
          "tool": "pylint"
        },
        {
          "code": "39             enemy.optional_attr = enemy.nonexistent_attribute\n40         except Exception:\n41             pass\n42 \n",
          "col_offset": 8,
          "end_col_offset": 16,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\arena.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 703,
            "link": "https://cwe.mitre.org/data/definitions/703.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Try, Except, Pass detected.",
          "line_number": 40,
          "line_range": [
            40,
            41
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b110_try_except_pass.html",
          "test_id": "B110",
          "test_name": "try_except_pass",
          "tool": "bandit"
        },
        {
          "code": "24         if color is None:\n25             color = random.choice(define.ALL_COLOR)\n26 \n",
          "col_offset": 20,
          "end_col_offset": 51,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 25,
          "line_range": [
            25
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "34         if pos is None:\n35             self.position = (random.randint(40, define.WIDTH - 40),\n36                              random.randint(40, define.HEIGHT - 40))\n",
          "col_offset": 29,
          "end_col_offset": 66,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 35,
          "line_range": [
            35
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "35             self.position = (random.randint(40, define.WIDTH - 40),\n36                              random.randint(40, define.HEIGHT - 40))\n37             self.is_big = False\n",
          "col_offset": 29,
          "end_col_offset": 67,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 36,
          "line_range": [
            36
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "39         else:\n40             self.position = (pos[0] + random.random() * 32 - 16,\n41                              pos[1] + random.random() * 32 - 16)\n",
          "col_offset": 38,
          "end_col_offset": 53,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
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
          "code": "40             self.position = (pos[0] + random.random() * 32 - 16,\n41                              pos[1] + random.random() * 32 - 16)\n42             self.is_big = True\n",
          "col_offset": 38,
          "end_col_offset": 53,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 41,
          "line_range": [
            41
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "42             self.is_big = True\n43         self.schedule_interval(self.update, random.random() * 0.2 + 0.1)\n44 \n",
          "col_offset": 44,
          "end_col_offset": 59,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\dot.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 43,
          "line_range": [
            43
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "15         self.is_dead = False\n16         self.angle = random.randrange(360)\n17         self.angle_dest = self.angle\n",
          "col_offset": 21,
          "end_col_offset": 42,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 16,
          "line_range": [
            16
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "18         # IndexError 检测\n19         self.color = random.choice(define.ALL_COLOR)\n20         self.no = Snake.no\n",
          "col_offset": 21,
          "end_col_offset": 52,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 19,
          "line_range": [
            19
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "22         if is_enemy:\n23             self.position = random.randrange(300, 1300), random.randrange(200, 600)\n24             if 600 < self.x < 1000:\n",
          "col_offset": 28,
          "end_col_offset": 55,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 23,
          "line_range": [
            23
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "22         if is_enemy:\n23             self.position = random.randrange(300, 1300), random.randrange(200, 600)\n24             if 600 < self.x < 1000:\n",
          "col_offset": 57,
          "end_col_offset": 83,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 23,
          "line_range": [
            23
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "26         else:\n27             self.position = random.randrange(700, 900), random.randrange(350, 450)\n28         self.is_enemy = is_enemy\n",
          "col_offset": 28,
          "end_col_offset": 54,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 27,
          "line_range": [
            27
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "26         else:\n27             self.position = random.randrange(700, 900), random.randrange(350, 450)\n28         self.is_enemy = is_enemy\n",
          "col_offset": 56,
          "end_col_offset": 82,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 27,
          "line_range": [
            27
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "55         if self.is_enemy:\n56             self.schedule_interval(self.ai, random.random() * 0.1 + 0.05)\n57 \n",
          "col_offset": 44,
          "end_col_offset": 59,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 56,
          "line_range": [
            56
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "180             if abs(angle - self.angle_dest) < 5:\n181                 self.angle_dest += random.randrange(90, 270)\n182 \n",
          "col_offset": 35,
          "end_col_offset": 60,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 330,
            "link": "https://cwe.mitre.org/data/definitions/330.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
          "line_number": 181,
          "line_range": [
            181
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random",
          "test_id": "B311",
          "test_name": "blacklist",
          "tool": "bandit"
        },
        {
          "code": "203                 self.unschedul_ai()\n204             except Exception:\n205                 pass\n206             arena = self.parent\n",
          "col_offset": 12,
          "end_col_offset": 20,
          "filename": "C:\\Users\\dell\\AppData\\Local\\Temp\\scan_sriucq0p\\snake.py",
          "issue_confidence": "HIGH",
          "issue_cwe": {
            "id": 703,
            "link": "https://cwe.mitre.org/data/definitions/703.html"
          },
          "issue_severity": "LOW",
          "issue_text": "Try, Except, Pass detected.",
          "line_number": 204,
          "line_range": [
            204,
            205
          ],
          "more_info": "https://bandit.readthedocs.io/en/1.8.6/plugins/b110_try_except_pass.html",
          "test_id": "B110",
          "test_name": "try_except_pass",
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
