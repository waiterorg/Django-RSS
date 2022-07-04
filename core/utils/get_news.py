from datetime import datetime
from time import mktime

import feedparser

from ..models import News, Rss


def get_news_from_rss_urls():
    """receives news from rss urls which are stored in rss table and it does not get repeated news"""
    rss_list = Rss.objects.filter(status=True)
    if rss_list.exists():
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


def get_all_news_query():
    """Query to get news from database"""
    return News.objects.all()
