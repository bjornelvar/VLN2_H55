from decimal import Decimal
from django.core.validators import MinValueValidator
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
    image = models.ImageField(upload_to='images/', default='images/no-image-default.png')
    listdate = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    # price = models.DecimalField(
    #     max_digits=15,
    #     decimal_places=1,
    #     validators=[MinValueValidator(Decimal('0.1'))]
    # ) # Nota þetta!! Þetta checkar hvort að talan sé yfir 0.1
    seller = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name
