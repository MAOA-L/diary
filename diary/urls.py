"""diary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views import static

from app_diary import urls as app_diary_urls
from api import urls as api_urls
from django.views.static import serve

from diary import settings
from diary.settings import MEDIA_ROOT
from app_upload import urls as upload_urls

urlpatterns = [
    path('', include(app_diary_urls)),
    path('api/', include(api_urls)),
    path('u/', include(upload_urls)),
    # path('upload', include(app_upload_urls)),
    # path('admin/', admin.site.urls),
    # path('xadmin/', xadmin.site.urls, name="xamdin"),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
