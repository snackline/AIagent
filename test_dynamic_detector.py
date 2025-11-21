#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试动态检测器
"""

import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from analyzers.dynamic_detector import (
    PythonDynamicDetector,
    JavaDynamicDetector,
    CppDynamicDetector
)


def test_python_dynamic_detector():
    """测试 Python 动态检测器"""
    print("=" * 60)
    print("测试 Python 动态检测器")
    print("=" * 60)
    
    # 测试代码示例
    test_code = '''
import os
import requests
from flask import request

# 1. 用户输入检测
def handle_request():
    # HTTP 请求参数
    user_input = request.args.get('query')
    
    # JSON 反序列化
    import json
    data = json.loads(user_input)
    
    # Cookie 操作
    cookie_val = request.cookies.get('session')

# 2. 资源管理检测
def file_operations():
    # 文件操作未使用 with
    f = open('test.txt', 'r')
    content = f.read()
    
    # 数据库连接
    import mysql.connector
    conn = mysql.connector.connect(host='localhost')

# 3. 并发检测
def threading_example():
    import threading
    t = threading.Thread(target=some_func)
    t.start()

# 4. 边界条件检测
def boundary_check():
    arr = [1, 2, 3]
    for i in range(10):
        print(arr[i])  # 可能越界
    
    # 除法操作
    result = 10 / x

# 5. 环境配置检测
def env_config():
    # 环境变量
    api_key = os.getenv('API_KEY')
    
    # 时间处理
    from datetime import datetime
    now = datetime.now()

# 6. 动态执行检测
def dynamic_exec():
    # eval
    result = eval(user_input)
    
    # exec
    exec(code_string)
    
    # pickle
    import pickle
    obj = pickle.loads(data)
'''
    
    files = [
        {
            "file": "test.py",
            "content": test_code
        }
    ]
    
    detector = PythonDynamicDetector(files)
    result = detector.detect_all()
    
    print(f"\n总共发现 {result['summary']['total']} 个问题")
    print(f"\n按类别统计:")
    for category, count in result['summary']['by_category'].items():
        print(f"  {category}: {count}")
    
    print(f"\n按严重程度统计:")
    for severity, count in result['summary']['by_severity'].items():
        print(f"  {severity}: {count}")
    
    print(f"\n详细问题列表:")
    for category, findings in result['categories'].items():
        if findings:
            print(f"\n{category} ({len(findings)} 个问题):")
            for i, finding in enumerate(findings[:5], 1):  # 只显示前5个
                print(f"  {i}. [{finding['severity']}] {finding['rule_id']}: {finding['message']}")
                print(f"     文件: {finding['file']}:{finding['line']}")


def test_java_dynamic_detector():
    """测试 Java 动态检测器"""
    print("\n" + "=" * 60)
    print("测试 Java 动态检测器")
    print("=" * 60)
    
    test_code = '''
import javax.servlet.http.*;
import java.sql.*;
import com.fasterxml.jackson.databind.ObjectMapper;

public class TestClass {
    // 1. 用户输入
    public void handleRequest(HttpServletRequest request) {
        String param = request.getParameter("id");
        String header = request.getHeader("Auth");
    }
    
    // 2. 资源管理
    public void fileOps() throws Exception {
        FileInputStream fis = new FileInputStream("test.txt");
        // 未使用 try-with-resources
    }
    
    // 3. 并发
    public void concurrency() {
        Thread t = new Thread(() -> {
            // 线程操作
        });
        t.start();
    }
    
    // 4. 动态执行
    public void reflection() throws Exception {
        Class<?> clazz = Class.forName(className);
        Method method = clazz.getDeclaredMethod(methodName);
        method.invoke(obj);
    }
}
'''
    
    files = [
        {
            "file": "TestClass.java",
            "content": test_code
        }
    ]
    
    detector = JavaDynamicDetector(files)
    result = detector.detect_all()
    
    print(f"\n总共发现 {result['summary']['total']} 个问题")
    print(f"\n按类别统计:")
    for category, count in result['summary']['by_category'].items():
        print(f"  {category}: {count}")
    
    print(f"\n详细问题列表:")
    for category, findings in result['categories'].items():
        if findings:
            print(f"\n{category} ({len(findings)} 个问题):")
            for i, finding in enumerate(findings[:3], 1):
                print(f"  {i}. [{finding['severity']}] {finding['rule_id']}: {finding['message']}")


def test_cpp_dynamic_detector():
    """测试 C++ 动态检测器"""
    print("\n" + "=" * 60)
    print("测试 C++ 动态检测器")
    print("=" * 60)
    
    test_code = '''
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 1. 用户输入
void user_input() {
    char buffer[100];
    gets(buffer);  // 不安全
    scanf("%s", buffer);  // 不安全
}

// 2. 资源管理
void resource_management() {
    char* ptr = (char*)malloc(100);
    // 可能忘记 free
    
    FILE* fp = fopen("test.txt", "r");
    // 可能忘记 fclose
}

// 3. 边界条件
void boundary_check() {
    int arr[10];
    for (int i = 0; i < 20; i++) {
        arr[i] = i;  // 数组越界
    }
}
'''
    
    files = [
        {
            "file": "test.cpp",
            "content": test_code
        }
    ]
    
    detector = CppDynamicDetector(files)
    result = detector.detect_all()
    
    print(f"\n总共发现 {result['summary']['total']} 个问题")
    print(f"\n按类别统计:")
    for category, count in result['summary']['by_category'].items():
        print(f"  {category}: {count}")
    
    print(f"\n详细问题列表:")
    for category, findings in result['categories'].items():
        if findings:
            print(f"\n{category} ({len(findings)} 个问题):")
            for i, finding in enumerate(findings[:3], 1):
                print(f"  {i}. [{finding['severity']}] {finding['rule_id']}: {finding['message']}")


if __name__ == '__main__':
    try:
        test_python_dynamic_detector()
        test_java_dynamic_detector()
        test_cpp_dynamic_detector()
        print("\n" + "=" * 60)
        print("所有测试完成！")
        print("=" * 60)
    except Exception as e:
        print(f"\n错误: {e}")
        import traceback
        traceback.print_exc()
