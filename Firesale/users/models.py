from django.db import models


# Create your models here.

class Profiles(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    passwordhash = models.CharField(max_length=500)
    bio = models.CharField(max_length=255, blank=True)
    rating = models.FloatField()
    online = models.BooleanField(default=False)
    image = models.ImageField(default=None)
