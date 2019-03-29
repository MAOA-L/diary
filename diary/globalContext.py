# -*- coding: utf-8 -*-
"""
 @Time    : 2019/2/12 21:58
 @Author  : CyanZoy
 @File    : globalContext.py
 @Software: PyCharm
 @Describe: 定义全局变量供模板直接使用
 """
from app_diary.models import BlogUser
from app_upload.models import Article, Sort


class Primary:
    user = BlogUser.objects.get(username="MAOA")
    article_count = Article.objects.count()
    sort_count = Sort.objects.count()
    global_context = {
        "primary": {
            "project_path": "http://localhost/",
            "project_name": "mydemo/",
            "author": user.username,
            "motto": user.motto,
            "article_count": article_count,
            "sort_count": sort_count
        },
        # "xadmin": {
        #     "title": "Blog后台管理",
        #     "name": "",
        #     "version": "0.01",
        #     "statistic": {
        #         "parent_id": 1,
        #         "current_id": 1,
        #         "url": "/xadmin",
        #         "title": "统计"
        #     },
        #     "publish": {
        #         "parent_id": 2,
        #         "current_id": 2,
        #         "url": "publish",
        #         "title": "文章发表",
        #     }
        # },
        'home': {
            'url': '/',
            'active': '',
        },
        'archive': {
            'url': '/archive',
            'active': '',
        },
        'categories': {
            'url': '/categories',
            'active': '',
        },
        'version': {
            'url': '/timeline',
            'active': '',
        },
        'search': {
            'url': '/search',
            'active': '',
        },


    }


def primary(*args):
    return Primary.global_context
