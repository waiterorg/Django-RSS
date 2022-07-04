from datetime import datetime
from time import mktime

import feedparser
from celery import shared_task
from celery.utils.log import get_task_logger
from django.db import transaction

from .models import News, Rss

logger = get_task_logger(__name__)


@shared_task
def get_news():
    try:
        rss_list = Rss.objects.filter(status=True)
        for rss in rss_list:
            url = rss.url
            feed = feedparser.parse(url)
            if feed["entries"]:
                for entry in feed["entries"]:
                    news, created = News.objects.get_or_create(
                        title=entry["title"],
                        published=datetime.fromtimestamp(
                            mktime(entry["published_parsed"])
                        ),
                    )
                    if created:
                        news.link = entry["link"]
                        news.description = entry["summary"]
                        news.creator = entry["author"]
                        news.save()
    except:
        logger.error("failed, there was an issue !")
