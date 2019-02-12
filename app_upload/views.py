from django.shortcuts import render, HttpResponse
import json
import re
from app_upload.util import (save_image, save_html)
from .models import Sort


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
