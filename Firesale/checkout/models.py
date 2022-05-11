from django.db import models
from users.models import Profiles
from items.models import Items


class ShippingInformation(models.Model):
    user = models.OneToOneField(Profiles, on_delete=models.CASCADE, primary_key=True)
    country = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state_province_region = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=150)
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
