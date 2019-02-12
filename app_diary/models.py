from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('用户名', max_length=255)
    icon = models.ImageField('头像地址', max_length=255)

    def __str__(self):
        return self.name


class AdminDiary(models.Model):
    header = models.CharField(max_length=255, verbose_name='HeadLine')
    text = models.TextField(null=True, verbose_name='Text')
    date = models.DateField(auto_now_add=True, verbose_name='Date')
    date_time = models.TimeField(auto_now_add=True, verbose_name='Time')
    share = models.BooleanField(verbose_name='Share(NO/YES?)')
    identification_id = models.CharField(max_length=255, default=None)

    class Meta:
        verbose_name = verbose_name_plural = '日记分享管理'


class Diary(models.Model):
    identification_id = models.CharField(max_length=255)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    header = models.CharField(max_length=255)
    text = models.TextField(null=True)
    audio = models.FilePathField(max_length=255, null=True)
    images = models.ImageField(null=True, upload_to='images/')
    code = models.CharField(max_length=255, null=True)
    sort = models.CharField(max_length=255, null=True)
    label = models.CharField(max_length=255, null=True)
    date = models.DateField(auto_now=True)
    date_time = models.TimeField(auto_now=True)
    order_num = models.IntegerField()

    class Meta:
        verbose_name = verbose_name_plural = '日记管理'


class Category(models.Model):
    name = models.CharField(max_length=255)


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Log(models.Model):
    date = models.DateField(auto_now=True)
    date_time = models.TimeField(auto_now=True)
    ip = models.GenericIPAddressField(auto_created=True)
    url = models.URLField(auto_created=True)
    name = models.CharField(max_length=255)




