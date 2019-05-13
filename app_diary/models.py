from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


# class User(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField('用户名', max_length=255)
#     icon = models.ImageField('头像地址', max_length=255)
#
#     def __str__(self):
#         return self.name


class BlogUser(AbstractUser, models.Model):
    id = models.AutoField("ID", primary_key=True)
    openId = models.CharField(max_length=50)
    gmtCreate = models.DateTimeField("创建时间", default=now)
    gmtModified = models.DateTimeField("修改时间", default=now)
    phoneNumber = models.CharField("手机号", max_length=20, rel=None)
    nickname = models.CharField('昵称', max_length=100, blank=True, rel=None)
    mugshot = models.ImageField('头像', upload_to='upload/mugshots', blank=True)
    motto = models.CharField('座右铭', max_length=255, null=True, rel=None)

    class Meta:
        db_table = "account_bloguser"


class AdminDiary(models.Model):
    header = models.CharField(max_length=255, verbose_name='HeadLine')
    text = models.TextField(null=True, verbose_name='Text')
    date = models.DateField(auto_now_add=True, verbose_name='Date')
    date_time = models.TimeField(auto_now_add=True, verbose_name='Time')
    share = models.BooleanField(verbose_name='Share(NO/YES?)')
    identification_id = models.CharField(max_length=255, default=None)

    class Meta:
        verbose_name = verbose_name_plural = '日记分享管理'


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




