from django.db import models
from django.utils import timezone


class TimeStamp(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Rss(TimeStamp):
    """
    store rss urls
    """

    name = models.CharField(max_length=200)
    url = models.URLField()
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "RSS Urls"

    def __str__(self):
        return f"{self.name} in {self.url} RSS"


class News(TimeStamp):
    """
    store news article
    """

    title = models.CharField(max_length=200)
    link = models.URLField()
    description = models.TextField()
    creator = models.CharField(max_length=200, blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "News Articles"

    def __str__(self):
        return self.title
