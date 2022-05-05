from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/', default='blank-profile-picture.png')
    rating = models.FloatField(null=True)

    def __str__(self):
        return self.user.username
