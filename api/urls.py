from django.urls import path

from api.views import CategoryList, NewsList, NewsDetail, NewsLike

urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('news/', NewsList.as_view()),
    path('news/<int:pk>', NewsDetail.as_view()),
    path('news/<int:pk>/like', NewsLike.as_view()),
]
