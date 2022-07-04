from celery import shared_task
from celery.utils.log import get_task_logger

from .utils.get_news import get_news_from_rss_urls

logger = get_task_logger(__name__)


@shared_task()
def get_news():
    try:
        get_news_from_rss_urls()
    except Exception as e:
        logger.error(f"failed ! error : {e}")
