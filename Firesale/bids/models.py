from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from users.models import Profiles
from items.models import Items


# Create your models here.

class Bids(models.Model):
    bidder = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    biddate = models.DateTimeField(auto_now=True)
    bidamount = models.DecimalField(
        max_digits=15,
        decimal_places=1,
        validators=[MinValueValidator(Decimal('0.1'))]
    )
    is_accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = (('bidder', 'item'),)

    def __str__(self):
        return f"{self.bidder} - {self.item} - {self.bidamount}"




