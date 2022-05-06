from django.db import models
from users.models import Profiles
from items.models import Items


# Create your models here.

class Bids(models.Model):
    bidder = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    biddate = models.DateTimeField(auto_now=True)
    bidamount = models.FloatField()

    class Meta:
        unique_together = (('bidder', 'item'),)


class Accepts(models.Model):
    bid = models.OneToOneField(Bids, on_delete=models.CASCADE)
    seller = models.OneToOneField(Profiles, on_delete=models.CASCADE)
    acceptdate = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField()

