from django.urls import path
from . import views
from items import views as item_views
from .forms.forms import ShippingForm, PaymentForm, ReviewForm, RateSellerForm
from .views import CheckoutWizard

urlpatterns = [
    path('', CheckoutWizard.as_view([ShippingForm, PaymentForm, RateSellerForm, ReviewForm]), name='checkout'),
]