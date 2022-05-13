from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm
from django_countries.fields import CountryField
from checkout.fields import CreditCardField, ExpiryDateField, VerificationValueField
from checkout.models import ShippingInformation
from items.models import Items


class ShippingForm(ModelForm):
    class Meta:
        model = ShippingInformation
        fields = ['first_name', 'last_name', 'address_1', 'address_2', 'city', 'zip', 'country', 'phone']


class PaymentForm(forms.Form):
    name_on_card = forms.CharField(max_length=50,
                                   required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'John Doe'}))
    card_number = CreditCardField(required=True,
                                  max_length=16,
                                  min_length=16,
                                  widget=forms.TextInput(attrs={'size': '16', 'placeholder': '1234 1234 1234 1234'}))
    expiry_date = ExpiryDateField(required=True)
    security_code = VerificationValueField(required=True,
                                           max_length=3,
                                           min_length=3,
                                           widget=forms.TextInput(attrs={'size': '3', 'placeholder': 'CVC'}))


class RateSellerForm(forms.Form):
    rating = forms.DecimalField(required=False, validators=[MinValueValidator(0.1), MaxValueValidator(5)])


class SoldForm(ModelForm):
    class Meta:
        model = Items
        exclude = ('category', 'name', 'seller', 'description', 'price', 'condition', 'date_added', 'has_accepted_bid')


class OrderForm(forms.Form):
    pass
