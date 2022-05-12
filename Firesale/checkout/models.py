from django.db import models
from django_countries.fields import CountryField

from users.models import Profiles
from items.models import Items


class ShippingInformation(models.Model):
    user = models.OneToOneField(Profiles, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = CountryField(blank_label='(Select country)')
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=15)


class Orders(models.Model):
    sender = models.ForeignKey(Profiles, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profiles, related_name='receiver', on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    is_sent = models.BooleanField(default=False)
    is_received = models.BooleanField(default=False)
    orderdate = models.DateTimeField(auto_now_add=True)
    sentdate = models.DateTimeField()
    receiveddate = models.DateTimeField()
    shipping_info = models.ForeignKey(ShippingInformation, on_delete=models.CASCADE)
