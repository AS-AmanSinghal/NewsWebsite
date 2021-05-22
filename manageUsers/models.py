from django.db import models


# Create your models here.

class ManageUsers(models.Model):
    name = models.TextField()
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name
