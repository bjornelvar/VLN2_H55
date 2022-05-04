from django.db import models
from users.models import Profiles


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=50)


class SubCategories(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Items(models.Model):
    subcategory = models.ForeignKey(SubCategories, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField()
    condition = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    listdate = models.DateField(auto_now_add=True)
    price = models.FloatField()
    seller = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    sold = models.BooleanField(default=False)
