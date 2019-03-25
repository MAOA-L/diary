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
        db_table = 'sort'


class Label(models.Model):
    """分类对应的标签"""
    label_feature = models.ForeignKey(Sort, on_delete=models.SET_NULL, to_field="sort_feature", blank=True, null=True, verbose_name="类别名")
    label_name = models.CharField(max_length=255, null=True, verbose_name="标签名")

    class Meta:
        verbose_name = verbose_name_plural = "标签"


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(max_length=36, unique=True, db_index=True)
    gmt_create = models.DateTimeField(auto_now_add=True)
    gmt_modified = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    text = models.TextField()
    sort = models.CharField(max_length=255)
    label = models.CharField(max_length=255, null=True)
    see_number = models.IntegerField(null=True)
    comment_number = models.IntegerField(null=True)

    class Meta:
        db_table = 'article'

