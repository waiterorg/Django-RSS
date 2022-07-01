from django.db import models
from django.utils import timezone


class Rss(models.Model):
    """ 
    store rss urls
    """
    name = models.CharField()
    url = models.URLField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} in {self.url} RSS"

class News(models.Model):
    """ 
    store news article 
    """
    title = models.CharField(max_length = 200) 
    link = models.URLField()
    description = models.TextField()
    creator = models.CharField(blank=True, null=True)
    published = models.DateTimeField(default = timezone.now)
    
    
    def __str__(self):
        return self.title
