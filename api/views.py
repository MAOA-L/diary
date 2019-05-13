import logging

from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.response import Response

from api.serilizer import ArticleSerializer, ArticleDetailSerializer
from app_upload.models import Article

logger = logging.getLogger('collect')


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveAPIView):
    # queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'uuid'

    def get(self, request, *args, **kwargs):
        logger.info("123456")
        obj = Article.objects.get(uuid=kwargs.get('uuid'))
        ser = ArticleDetailSerializer(instance=obj, many=False)
        # ret = json.dumps(ser.data, ensure_ascii=False)
        return Response(ser.data)
