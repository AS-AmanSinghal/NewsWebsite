from django.db import models


# Create your models here.

class NewsAppModel(models.Model):
    name = models.TextField(max_length=255)
    about = models.TextField(max_length=255, default='-')
    fb = models.TextField(max_length=255, default='http://fb.com/')
    twitter = models.TextField(max_length=255, default='http://twitter.com/')
    youtube = models.TextField(max_length=255, default='http://youtube.com/')

    def __str__(self):
        return self.name
