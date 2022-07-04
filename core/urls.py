from django.urls import path

from .views import NewsList, UpdateNews

urlpatterns = [
    path("", UpdateNews.as_view()),
    path("news/", NewsList.as_view()),
]
