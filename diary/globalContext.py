# -*- coding: utf-8 -*-
"""
 @Time    : 2019/2/12 21:58
 @Author  : CyanZoy
 @File    : globalContext.py
 @Software: PyCharm
 @Describe: 定义全局变量供模板直接使用
 """


def primary(request):
    return {"primary": {
        "project_home_path": "localhost"
    }}
