import imp

from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            "title",
            "link",
            "description",
            "creator",
            "published",
        ]
        read_only = True
