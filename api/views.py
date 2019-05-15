import logging

from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from api.serilizer import ArticleSerializer, ArticleDetailSerializer, ArticleDetailCreateSerializer
from app_upload.models import Article

logger = logging.getLogger('collect')


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    # queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'uuid'

    def get(self, request, *args, **kwargs):
        logger.info("123456")
        obj = Article.objects.get(uuid=kwargs.get('uuid'))
        ser = ArticleDetailSerializer(instance=obj, many=False)
        # ret = json.dumps(ser.data, ensure_ascii=False)
        return Response(ser.data)

    def post(self, request, *args, **kwargs):
        self.serializer_class = ArticleDetailCreateSerializer
        return super().post(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print(request.user)
        self.queryset = Article.objects.all()
        return super().put(request, *args, **kwargs)

