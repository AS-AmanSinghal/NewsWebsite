from django.db import models


# Create your models here.

class SubCategory(models.Model):
    category_id = models.IntegerField()
    category = models.CharField(max_length=25)
    subcategory = models.CharField(max_length=25)

    def __str__(self):
        return self.subcategory
