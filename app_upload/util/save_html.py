# -*- coding: utf-8 -*-
"""
 @Time    : 2018/12/17 14:17
 @Author  : CyanZoy
 @File    : save_html.py
 @Software: PyCharm
 """
from lxml import etree
from app_upload.models import Article
import uuid


class Save:
    article = Article()
    article.article_feature = uuid.uuid1()
    article.article_sort = None
    article.article_label = None
    article.article_see = 0
    article.article_comment = 0

    def __init__(self, article_sort=None, article_label=None):
        if isinstance(self.article, Article):
            self.article = Article()
            self.article.article_feature = uuid.uuid1()
            self.article.article_sort = None
            self.article.article_label = None
            self.article.article_see = 0
            self.article.article_comment = 0
        if article_sort:
            self.article.article_sort = article_sort
        if article_label:
            self.article.article_label = article_label

    def save(self, article_data):
        article_html = article_data.read().decode('utf-8')
        # 全部
        self.article.article_html = article_html
        # 解析出主题名
        parse_html = etree.HTML(article_html).xpath('//theory')
        self.article.article_theory = parse_html[0].text if parse_html else 'NULL'

        print(self.article.article_theory)
        self.article.save()



