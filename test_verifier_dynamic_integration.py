#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试验证器动态检测集成
"""

import sys
import os
import tempfile
import shutil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from verifiers.python_verifier import PythonVerifier
from utils.language_detector import Language


def test_verifier_with_dynamic_testing():
    """测试验证器集成动态检测"""
    print("=" * 70)
    print("测试：验证器 + 动态检测集成")
    print("=" * 70)
    
    # 创建临时源文件夹
    source_folder = tempfile.mkdtemp(prefix="test_source_")
    
    try:
        # 创建一个有问题的 Python 文件
        buggy_code = '''
def divide(a, b):
    """除法函数 - 存在除零风险"""
    return a / b  # 未检查 b == 0

def get_config():
    """获取配置 - 缺少默认值"""
    import os
    return os.environ['API_KEY']  # 可能不存在

def unsafe_eval(code):
    """不安全的动态执行"""
    return eval(code)  # 危险！

counter = 0
def increment():
    """计数器 - 线程不安全"""
    global counter
    counter += 1
'''
        
        # 修复后的代码
        fixed_code = '''
def divide(a, b):
    """除法函数 - 已修复"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

def get_config():
    """获取配置 - 已添加默认值"""
    import os
    return os.environ.get('API_KEY', 'default_key')

def unsafe_eval(code):
    """不安全的动态执行 - 已移除"""
    # 不再使用 eval
    raise NotImplementedError("已禁用动态执行")

import threading
counter_lock = threading.Lock()
counter = 0

def increment():
    """计数器 - 已添加锁"""
    global counter
    with counter_lock:
        counter += 1
'''
        
        # 写入源文件
        test_file_path = os.path.join(source_folder, "app.py")
        with open(test_file_path, 'w', encoding='utf-8') as f:
            f.write(buggy_code)
        
        print(f"✅ 创建测试源文件: {test_file_path}")
        
        # 准备文件信息
        original_file = {
            "file": test_file_path,
            "content": buggy_code
        }
        
        fixed_file = {
            "file": test_file_path,
            "content": fixed_code,
            "original_content": buggy_code
        }
        
        # 模拟原始问题
        original_issues = [
            {"rule_id": "DIV-001", "line": 4, "message": "除零风险"},
            {"rule_id": "ENV-001", "line": 9, "message": "环境变量缺失"},
            {"rule_id": "EXEC-001", "line": 13, "message": "使用 eval"},
            {"rule_id": "CONC-001", "line": 19, "message": "线程不安全"},
        ]
        
        # 创建验证器
        verifier = PythonVerifier()
        
        print(f"\n开始验证（启用动态测试）...")
        
        # 运行验证（启用动态测试）
        result = verifier.verify(
            original_file=original_file,
            fixed_file=fixed_file,
            original_issues=original_issues,
            test_cases=None,
            scanner=None,
            enable_dynamic_testing=True,
            source_folder=source_folder
        )
        
        # 显示结果
        print(f"\n{'=' * 70}")
        print("验证结果:")
        print(f"{'=' * 70}")
        print(f"  文件: {result.file}")
        print(f"  编译成功: {result.compile_success}")
        print(f"  测试成功: {result.test_success}")
        print(f"  修复率: {result.fix_rate:.1f}%")
        
        if hasattr(result, 'dynamic_test_result') and result.dynamic_test_result:
            dyn = result.dynamic_test_result
            print(f"\n动态测试结果:")
            print(f"  启用: {dyn.get('enabled', False)}")
            print(f"  总测试数: {dyn.get('total_tests', 0)}")
            print(f"  通过: {dyn.get('passed', 0)}")
            print(f"  失败: {dyn.get('failed', 0)}")
            print(f"  发现问题: {dyn.get('total_issues', 0)}")
            
            if dyn.get('by_category'):
                print(f"\n  按类别统计:")
                for category, stats in dyn['by_category'].items():
                    print(f"    {category}: {stats.get('issues', 0)} 个问题")
        else:
            print(f"\n⚠️ 没有动态测试结果")
        
        print(f"\n{'=' * 70}")
        print("✅ 测试完成!")
        print(f"{'=' * 70}")
        
    finally:
        # 清理临时文件夹
        if os.path.exists(source_folder):
            shutil.rmtree(source_folder)
            print(f"\n已清理临时文件夹: {source_folder}")


def test_folder_copy_with_fixes():
    """测试文件夹复制和修复应用"""
    print("\n" + "=" * 70)
    print("测试：文件夹复制 + 修复应用")
    print("=" * 70)
    
    source_folder = tempfile.mkdtemp(prefix="test_source_")
    
    try:
        # 创建源文件夹结构
        os.makedirs(os.path.join(source_folder, "src"), exist_ok=True)
        os.makedirs(os.path.join(source_folder, "tests"), exist_ok=True)
        
        # 创建多个文件
        files_to_create = {
            "src/main.py": "print('original main')",
            "src/utils.py": "def helper(): pass",
            "tests/test_main.py": "# test",
            "README.md": "# Project"
        }
        
        for rel_path, content in files_to_create.items():
            full_path = os.path.join(source_folder, rel_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        print(f"✅ 创建源文件夹结构: {source_folder}")
        for path in files_to_create.keys():
            print(f"  - {path}")
        
        # 准备修复后的文件
        fixed_files = [
            {
                "file": os.path.join(source_folder, "src/main.py"),
                "content": "print('fixed main')\nprint('with changes')"
            },
            {
                "file": os.path.join(source_folder, "src/utils.py"),
                "content": "def helper():\n    return 'fixed'"
            }
        ]
        
        # 使用验证器的方法复制文件夹
        verifier = PythonVerifier()
        temp_folder = verifier._copy_folder_with_fixes(source_folder, fixed_files)
        
        if temp_folder:
            print(f"\n✅ 成功复制到: {temp_folder}")
            
            # 验证文件内容
            print(f"\n验证修复后的文件:")
            for fixed_file in fixed_files:
                rel_path = os.path.relpath(fixed_file['file'], source_folder)
                temp_file = os.path.join(temp_folder, rel_path)
                
                if os.path.exists(temp_file):
                    with open(temp_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    print(f"  ✅ {rel_path}: 已应用修复")
                    print(f"     内容: {content[:50]}...")
                else:
                    print(f"  ❌ {rel_path}: 文件不存在")
            
            # 验证其他文件也被复制
            print(f"\n验证其他文件:")
            other_file = os.path.join(temp_folder, "README.md")
            if os.path.exists(other_file):
                print(f"  ✅ README.md: 已复制")
            
            # 清理
            shutil.rmtree(os.path.dirname(temp_folder))
        else:
            print(f"\n❌ 复制失败")
        
    finally:
        if os.path.exists(source_folder):
            shutil.rmtree(source_folder)


if __name__ == '__main__':
    try:
        test_folder_copy_with_fixes()
        test_verifier_with_dynamic_testing()
        
        print("\n" + "=" * 70)
        print("🎉 所有测试完成!")
        print("=" * 70)
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
