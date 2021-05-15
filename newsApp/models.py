from django.db import models


# Create your models here.

class NewsAppModel(models.Model):
    name = models.CharField(max_length=30)
    about = models.TextField(max_length=255, default='-')
    fb = models.CharField(max_length=50, default='http://fb.com/')
    twitter = models.CharField(max_length=50, default='http://twitter.com/')
    youtube = models.CharField(max_length=50, default='http://youtube.com/')
    contactNumber = models.CharField(max_length=13, default='+91')

    def __str__(self):
        return self.name
