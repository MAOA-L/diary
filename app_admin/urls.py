# -*- coding: utf-8 -*-
"""
 @Time    : 2019/2/16 16:24
 @Author  : CyanZoy
 @File    : urls.py
 @Software: PyCharm
 """
from django.conf import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('statistic', views.index),
    path('publish', views.publish),

]
