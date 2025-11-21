#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
综合验证测试 - 动态检测功能
Comprehensive Validation Test - Dynamic Detection Features
"""

import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_module_imports():
    """测试模块导入"""
    print("=" * 70)
    print("测试 1: 模块导入 (Module Imports)")
    print("=" * 70)
    
    try:
        from analyzers.dynamic_detector import (
            DynamicDetector,
            PythonDynamicDetector,
            JavaDynamicDetector,
            CppDynamicDetector,
            DynamicFinding
        )
        print("✅ 所有检测器类导入成功")
        return True
    except Exception as e:
        print(f"❌ 导入失败: {e}")
        return False


def test_detection_categories():
    """测试所有检测类别"""
    print("\n" + "=" * 70)
    print("测试 2: 检测类别覆盖 (Detection Categories)")
    print("=" * 70)
    
    from analyzers.dynamic_detector import PythonDynamicDetector
    
    test_code = '''
import requests
import pickle
import threading
import os
from datetime import datetime

# 1. 用户输入
user_input = request.args.get('query')
data = json.loads(user_input)

# 2. 资源管理
f = open('test.txt', 'r')
conn = mysql.connector.connect()

# 3. 并发
t = threading.Thread(target=func)

# 4. 边界条件
for i in range(10):
    arr[i] = i
result = 10 / x

# 5. 环境配置
api_key = os.getenv('API_KEY')
now = datetime.now()

# 6. 动态执行
eval(user_input)
pickle.loads(data)
'''
    
    files = [{"file": "test.py", "content": test_code}]
    detector = PythonDynamicDetector(files)
    result = detector.detect_all()
    
    categories = result['categories']
    required_categories = [
        'user_input',
        'resource_management', 
        'concurrency',
        'boundary_conditions',
        'environment_config',
        'dynamic_execution'
    ]
    
    all_present = True
    for cat in required_categories:
        count = len(categories.get(cat, []))
        status = "✅" if count > 0 else "❌"
        print(f"  {status} {cat}: {count} 个问题")
        if count == 0:
            all_present = False
    
    print(f"\n总计: {result['summary']['total']} 个问题")
    print(f"  高危: {result['summary']['by_severity']['HIGH']}")
    print(f"  中危: {result['summary']['by_severity']['MEDIUM']}")
    print(f"  低危: {result['summary']['by_severity']['LOW']}")
    
    return all_present


def test_integration_with_scanners():
    """测试与现有扫描器的集成"""
    print("\n" + "=" * 70)
    print("测试 3: 扫描器集成 (Scanner Integration)")
    print("=" * 70)
    
    from analyzers.defect_scanner import DefectScanner
    
    test_files = [
        {
            "file": "app.py",
            "content": '''
import pickle
f = open('test.txt')
eval(user_input)
'''
        }
    ]
    
    scanner = DefectScanner(test_files)
    result = scanner.scan(enable_dynamic=True)
    
    # 检查动态检测结果
    has_dynamic = 'dynamic' in result
    if has_dynamic:
        dynamic_result = result['dynamic']
        has_detection = 'dynamic_detection' in dynamic_result
        
        if has_detection:
            detection = dynamic_result['dynamic_detection']
            enabled = detection.get('enabled', False)
            total = detection.get('summary', {}).get('total', 0)
            
            print(f"✅ DefectScanner 集成成功")
            print(f"  动态检测启用: {enabled}")
            print(f"  检测到问题: {total}")
            return True
        else:
            print(f"⚠️ dynamic_detection 未找到，但有其他动态检测")
            return True
    else:
        print("❌ 没有动态检测结果")
        return False


def test_severity_levels():
    """测试严重程度分级"""
    print("\n" + "=" * 70)
    print("测试 4: 严重程度分级 (Severity Levels)")
    print("=" * 70)
    
    from analyzers.dynamic_detector import PythonDynamicDetector
    
    # 高危问题 - eval
    # 中危问题 - 线程创建
    # 低危问题 - 环境变量无默认值
    test_code = '''
import os
import threading

# 高危
eval(user_input)

# 中危
t = threading.Thread(target=func)

# 低危
key = os.getenv('KEY')
'''
    
    test_files = [
        {
            "file": "test.py",
            "content": test_code
        }
    ]
    
    detector = PythonDynamicDetector(test_files)
    result = detector.detect_all()
    
    has_high = result['summary']['by_severity']['HIGH'] > 0
    has_medium = result['summary']['by_severity']['MEDIUM'] > 0
    has_low = result['summary']['by_severity']['LOW'] > 0
    
    print(f"  {'✅' if has_high else '❌'} 检测到高危问题: {result['summary']['by_severity']['HIGH']}")
    print(f"  {'✅' if has_medium else '❌'} 检测到中危问题: {result['summary']['by_severity']['MEDIUM']}")
    print(f"  {'✅' if has_low else '❌'} 检测到低危问题: {result['summary']['by_severity']['LOW']}")
    
    return has_high and has_medium and has_low


def test_fix_suggestions():
    """测试修复建议"""
    print("\n" + "=" * 70)
    print("测试 5: 修复建议 (Fix Suggestions)")
    print("=" * 70)
    
    from analyzers.dynamic_detector import PythonDynamicDetector
    
    files = [
        {
            "file": "test.py",
            "content": "eval(user_input)"
        }
    ]
    
    detector = PythonDynamicDetector(files)
    result = detector.detect_all()
    
    # 检查是否有修复建议
    has_suggestions = False
    for category, findings in result['categories'].items():
        for finding in findings:
            if finding.get('suggestion'):
                has_suggestions = True
                print(f"✅ 问题: {finding['message']}")
                print(f"  建议: {finding['suggestion']}")
                break
        if has_suggestions:
            break
    
    if not has_suggestions:
        print("❌ 未找到修复建议")
    
    return has_suggestions


def test_multi_language_support():
    """测试多语言支持"""
    print("\n" + "=" * 70)
    print("测试 6: 多语言支持 (Multi-Language Support)")
    print("=" * 70)
    
    from analyzers.dynamic_detector import (
        PythonDynamicDetector,
        JavaDynamicDetector,
        CppDynamicDetector
    )
    
    # Python
    py_files = [{"file": "test.py", "content": "eval(user_input)"}]
    py_detector = PythonDynamicDetector(py_files)
    py_result = py_detector.detect_all()
    py_works = py_result['enabled'] and py_result['summary']['total'] > 0
    print(f"  {'✅' if py_works else '❌'} Python 检测器: {py_result['summary']['total']} 问题")
    
    # Java
    java_files = [{"file": "Test.java", "content": 'String param = request.getParameter("id");'}]
    java_detector = JavaDynamicDetector(java_files)
    java_result = java_detector.detect_all()
    java_works = java_result['enabled'] and java_result['summary']['total'] > 0
    print(f"  {'✅' if java_works else '❌'} Java 检测器: {java_result['summary']['total']} 问题")
    
    # C++
    cpp_files = [{"file": "test.cpp", "content": "gets(buffer);"}]
    cpp_detector = CppDynamicDetector(cpp_files)
    cpp_result = cpp_detector.detect_all()
    cpp_works = cpp_result['enabled'] and cpp_result['summary']['total'] > 0
    print(f"  {'✅' if cpp_works else '❌'} C++ 检测器: {cpp_result['summary']['total']} 问题")
    
    return py_works and java_works and cpp_works


def main():
    """运行所有测试"""
    print("\n" + "=" * 70)
    print("动态检测功能 - 综合验证测试")
    print("Dynamic Detection - Comprehensive Validation")
    print("=" * 70)
    
    tests = [
        ("模块导入", test_module_imports),
        ("检测类别", test_detection_categories),
        ("扫描器集成", test_integration_with_scanners),
        ("严重程度", test_severity_levels),
        ("修复建议", test_fix_suggestions),
        ("多语言支持", test_multi_language_support),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ 测试 '{name}' 失败: {e}")
            import traceback
            traceback.print_exc()
            results.append((name, False))
    
    # 汇总结果
    print("\n" + "=" * 70)
    print("测试结果汇总 (Test Summary)")
    print("=" * 70)
    
    passed = sum(1 for _, r in results if r)
    total = len(results)
    
    for name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"  {status} - {name}")
    
    print("\n" + "=" * 70)
    print(f"总计: {passed}/{total} 测试通过")
    print("=" * 70)
    
    if passed == total:
        print("\n🎉 所有测试通过！动态检测功能工作正常。")
        return 0
    else:
        print(f"\n⚠️ {total - passed} 个测试失败，需要修复。")
        return 1


if __name__ == '__main__':
    sys.exit(main())
