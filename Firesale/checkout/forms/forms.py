from django import forms
from django_countries.fields import CountryField

from checkout.fields import CreditCardField, ExpiryDateField, VerificationValueField


class ShippingForm(forms.Form):
    full_name = forms.CharField(required=True)
    address_1 = forms.CharField(required=True)
    address_2 = forms.CharField(required=False)
    city = forms.CharField(required=True)
    country = CountryField(blank_label='(Select country)').formfield()
    zip = forms.CharField(required=True, widget=forms.TextInput(attrs={'size': 6}))


class BillingForm(forms.Form):
    full_name = forms.CharField(required=True)
    billing_address = forms.CharField(required=True)
    city = forms.CharField(required=True)
    country = CountryField(blank_label='(Select country)').formfield()
    zip = forms.CharField(required=True, widget=forms.TextInput(attrs={'size': 6}))


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


