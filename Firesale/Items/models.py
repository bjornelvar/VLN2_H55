from django.db import models
from users.models import Profiles


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SubCategories(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Items(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/', default='no-image-default.png')
    listdate = models.DateField(auto_now_add=True)
    price = models.FloatField()
    seller = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name
