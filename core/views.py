from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News
from .serializers import NewsSerializer
from .tasks import get_news


class UpdateNews(APIView):
    def post(self, request):
        get_news.delay()
        return Response({"msg": "ok"})


class NewsList(APIView, PageNumberPagination):
    """
    Return list of all news with pagination
    """

    # TODO:
    # 1. [] jwt auth permision for access
    # 2. [x] Create serializer
    # 3. [x] drf pagination
    def get(self, request):
        paginator = PageNumberPagination
        news = News.objects.all()
        result = self.paginate_queryset(news, request, view=self)
        serializer = NewsSerializer(result, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response
