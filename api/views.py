from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from api.filters import NewsFilter
from api.models import Category, News
from api.serializers import CategorySerializer, NewsSerializer


# Create your views here.


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # filterset_fields = ('language',)


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filterset_class = NewsFilter


class NewsDetail(APIView):
    def get_object(self, pk):
        try:
            return News.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        news = self.get_object(pk)
        news.view += 1
        news.save()
        serializer = NewsSerializer(news)
        return Response(serializer.data)


class NewsLike(APIView):
    def get_object(self, pk):
        try:
            return News.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        news = self.get_object(pk)
        news.like += 1
        news.save()
        serializer = NewsSerializer(news)
        return Response(serializer.data)
