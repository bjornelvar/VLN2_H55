from django import forms
from django_countries.fields import CountryField


class ShippingForm(forms.Form):
    full_name = forms.CharField()
    address_1 = forms.CharField()
    address_2 = forms.CharField(required=False)
    city = forms.CharField()
    country = CountryField(blank_label='(select country)').formfield()
    zip = forms.CharField()


class BillingForm(forms.Form):
    full_name = forms.CharField()
    billing_address = forms.CharField()
    city = forms.CharField()
    country = CountryField(blank_label='(select country)').formfield()
    zip = forms.CharField()
#
#
# class PaymentForm(forms.Form):
#     stripe_id = forms.CharField()
#     card_number = forms.CharField()
#     card_cvc = forms.CharField()
#     card_expiry_date = forms.CharField()
#     card_name = forms.CharField()
#     card_address_line_1 = forms.CharField()
#     card_address_line_2 = forms.CharField(required=False)
#     card_city = forms.CharField()
#     card_state = forms.CharField()
#     card_postal_code = forms.CharField()
#     card_country = CountryField(blank_label='(select country)').formfield()


