from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News
from .serializers import NewsSerializer
from .tasks import get_news


class UpdateNews(APIView):
    def post(self, request):
        get_news.delay()
        return Response({"msg": "ok"})


class NewsList(APIView):
    """
    Return list of all news with pagination
    """

    # TODO:
    # 1. [] jwt auth permision for access
    # 2. [] Create serializer
    # 3. [] drf pagination
    def get(self, request):
        queryset = News.objects.all()
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data)
