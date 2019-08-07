# -*- coding: utf-8 -*-
"""
 @Time    : 2019/4/28 11:11
 @Author  : CyanZoy
 @File    : serilizer.py
 @Software: PyCharm
 """
from rest_framework import serializers

from app_upload.models import Article
import re


class ArticleSerializer(serializers.ModelSerializer):
    gmt_create = serializers.SerializerMethodField(label="时间")
    link = serializers.HyperlinkedIdentityField(view_name='article-detail', lookup_field='uuid', lookup_url_kwarg='uuid')

    class Meta:
        model = Article
        fields = ('id', 'uuid', 'gmt_create', 'username', 'title', 'link', 'sort', 'label', 'see_number', 'comment_number')

    def get_gmt_create(self, obj):
        return obj.gmt_create.strftime('%Y-%m-%d')


class ArticleDetailSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField(label='内容')

    class Meta:
        model = Article
        fields = ('uuid', 'gmt_create', 'title', 'sort', 'see_number', 'comment_number', 'text', 'username')

    def get_text(self, obj):
        return re.compile(r'<[^>]+>').sub('', obj.text)


class ArticleDetailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('uuid', 'gmt_create', 'title', 'sort', 'see_number', 'comment_number', 'text', )
