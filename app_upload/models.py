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
    sort_feature = models.CharField(max_length=240, unique=True, verbose_name="类别编号")
    # 分类名称
    sort_name = models.CharField(max_length=255, verbose_name="类别名称")

    def __str__(self):
        return self.sort_name

    class Meta:
        verbose_name_plural = verbose_name = "文章分类"


class Label(models.Model):
    """分类对应的标签"""
    label_feature = models.ForeignKey(Sort, on_delete=models.SET_NULL, to_field="sort_feature", blank=True, null=True, verbose_name="类别名")
    label_name = models.CharField(max_length=255, null=True, verbose_name="标签名")

    class Meta:
        verbose_name = verbose_name_plural = "标签"


class Article(models.Model):
    """文章"""
    # 文章的编号
    article_feature = models.CharField(max_length=100, primary_key=True, verbose_name="文章编号")
    # 文章标题
    article_title = models.CharField(max_length=255, null=True, verbose_name="文章标题")

    # 文章长度

    # 文章的分类
    article_sort = models.ForeignKey(Sort, on_delete=models.SET_NULL, to_field="sort_feature", blank=True, null=True, verbose_name="分类")
    # 文章的标签
    article_label = models.CharField(max_length=255, null=True, verbose_name="标签")
    # 文章发表时间
    article_time = models.DateField(auto_now_add=True, verbose_name="发表时间")
    # 文章浏览数
    article_see = models.IntegerField(verbose_name="浏览数")
    # 文章评论数
    article_comment = models.IntegerField()
    # 文章主题
    article_theory = models.TextField(verbose_name="文章主题")
    # 文章网页代码
    article_html = models.TextField(verbose_name="文章内容")



