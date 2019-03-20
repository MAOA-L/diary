# -*- coding: utf-8 -*-
"""
 @Time    : 2018/8/18 22:44
 @Author  : CyanZoy
 @File    : urls.py
 @Describe:
 """
from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('', index),
    path('reward/search', search),
    path('articles/<str:uuid>', detail),
    path('archive', archive),
    path('categories', categories),
    path('categories/<str:name>/', categories_list),
    path('search', search),
    path('search/<str:art>', search_result),
    path('timeline', timeline)
]
