from django.db import models


# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    website = models.CharField(max_length=150)
    message = models.TextField(default='')

    def __str__(self):
        return self.name
