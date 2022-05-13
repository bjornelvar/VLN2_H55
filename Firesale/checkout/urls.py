from django.urls import path
from . import views
from items import views as item_views
from .forms.forms import ShippingForm, PaymentForm, RateSellerForm, SoldForm
from .views import CheckoutWizard
from .views import FORMS

urlpatterns = [
    path('<int:id>', CheckoutWizard.as_view(FORMS), name='checkout'),

]