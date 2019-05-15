from django.core.cache import cache
from django.shortcuts import render, HttpResponse
import json
import re

from django.views.decorators.cache import cache_page

from app_upload.util import (save_image, save_html)
from .models import Sort
import requests


def index(request):
    if request.method == 'POST':
        myfile = request.FILES.get('file_data', None)
        file_type = re.search('\.(.*)', str(myfile)).group(1)
        if file_type in ['jpg', 'jpeg', 'png', 'PNG', 'JPG', 'JPEG']:
            save_image.save(myfile, str(myfile)[-3:])
            print('图片')
        elif file_type in ['html', 'htm', 'HTM', 'HTML']:
            article = save_html.Save(article_sort=Sort.objects.get(sort_name='Python'), article_label='django')
            print('aaaa=', article)
            article.save(myfile)
        return HttpResponse(json.dumps(False))
    else:
        result = [w for w in Sort.objects.all().values('id', 'sort_feature', 'sort_name')]

    return render(request, 'upload/upload.html', {'sort': result})


def test(request):
    return render(request, "upload/test.html", {})


@cache_page(timeout=5, cache='default', key_prefix='accesstoken')
def cache(request):
    import time
    return HttpResponse(AccT().get_acc())


class AccT:
    """accstoken管理"""
    def __init__(self):
        self.APPID = 'wxcaaee441b8a862b8'
        self.APPSECRET = 'db6e5e059073ed593513efdb3718aaf9'
        self.url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'

    def get_acc(self):
        """
        获取access token
        :return: access token
        """
        result = requests.get(self.url.format(self.APPID, self.APPSECRET)).content.decode('utf-8')
        return json.loads(result)
