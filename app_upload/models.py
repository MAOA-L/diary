from django.db import models


class UploadImage(models.Model):
    # 上传时间
    date = models.DateField(auto_now=True)
    # 文件大小（kb）
    size = models.IntegerField()
    # 压缩后文件大小（bit）
    compress_size = models.IntegerField(null=True)
    # 原图片分辨率
    resolution = models.CharField(max_length=255)
    # 原图路径
    path = models.CharField(max_length=255)
    # 原图片分辨率
    compress_resolution = models.CharField(max_length=255)
    # 缩略图路径
    compress_path = models.CharField(max_length=255)
    # 图片别名/备注
    alias = models.CharField(max_length=255, null=True)


class Sort(models.Model):
    """分类"""
    # 分类编号
    sort_feature = models.CharField(max_length=240, unique=True)
    # 分类名称
    sort_name = models.CharField(max_length=255)


class Label(models.Model):
    """分类对应的标签"""
    label_feature = models.ForeignKey(Sort, on_delete=models.SET_NULL, to_field="sort_feature", blank=True, null=True)
    label_name = models.CharField(max_length=255, null=True)


class Article(models.Model):
    """文章"""
    # 文章的编号
    article_feature = models.CharField(max_length=100, primary_key=True)
    # 文章长度

    # 文章的分类
    article_sort = models.ForeignKey(Sort, on_delete=models.SET_NULL, to_field="sort_feature", blank=True, null=True)
    # 文章的标签
    article_label = models.CharField(max_length=255, null=True)
    # 文章发表时间
    article_time = models.DateField(auto_now_add=True)
    # 文章浏览数
    article_see = models.IntegerField()
    # 文章评论数
    article_comment = models.IntegerField()
    # 文章主题
    article_theory = models.TextField()
    # 文章网页代码
    article_html = models.TextField()



