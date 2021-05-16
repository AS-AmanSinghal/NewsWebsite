from django.db import models


# Create your models here.

class LatestNews(models.Model):
    name = models.CharField(max_length=50)
    short_text = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    date = models.CharField(max_length=12)
    image = models.TextField(max_length=2048)
    writer = models.CharField(max_length=50)
    imageName = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name
