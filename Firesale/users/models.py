from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

# Create your models here.

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='images/', default='images/blank-profile-picture.png')
    rating = models.FloatField(null=True)

    def __str__(self):
        return self.user.username

class Review(models.Model):
    reviewed = models.ForeignKey(User, related_name='reviewed', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, related_name='reviewer', on_delete=models.CASCADE)
    review = models.CharField(max_length=255)
    reviewdate = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(
        max_digits=1,
        decimal_places=1,
        validators=[MinValueValidator(Decimal('0.0')), MaxValueValidator(Decimal('5.0'))],
        null=True
    )

