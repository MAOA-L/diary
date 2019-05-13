# -*- coding: utf-8 -*-
"""
 @Time    : 2019/4/28 11:39
 @Author  : CyanZoy
 @File    : urls.py
 @Software: PyCharm
 """
from django.urls import path

from api.views import ArticleList, ArticleDetail

urlpatterns = [
    path('article/', ArticleList.as_view(), name='article-list'),
    path('article/detail/<str:uuid>/', ArticleDetail.as_view(), name='article-detail')
]
