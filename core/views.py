from django.http import HttpResponse
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News
from .serializers import NewsSerializer
from .tasks import get_news


class UpdateNews(APIView):
    """
    Update and get news from rss urls.
    """

    def post(self, request):
        get_news.delay()
        response = Response(
            {"message": "the request was successfull !"},
            status=status.HTTP_200_OK,
        )
        return response


class NewsList(APIView, PageNumberPagination):
    """
    Return list of all news with pagination.
    """

    permission_classes = (IsAuthenticated,)
    news_serializer = NewsSerializer

    def get(self, request):
        news = News.objects.all()
        result = self.paginate_queryset(news, request, view=self)
        serializer = self.news_serializer(result, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response
