from django.db import models


# Create your models here.

class Profiles(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='profile_pics/', default='blank-profile-picture.png')
    rating = models.FloatField()
    online = models.BooleanField(default=False)
