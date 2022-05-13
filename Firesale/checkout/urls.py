from django.urls import path
from . import views
from items import views as item_views
from .forms.forms import ShippingForm, PaymentForm, RateSellerForm, SoldForm
from .views import CheckoutWizard
from .views import FORMS

urlpatterns = [
    path('<int:id>', CheckoutWizard.as_view(FORMS), name='checkout'),
    # path('review/', views.review_view, name='review'),
    # path('success/', views.success_view, name='success'),
    # path('shipping/', views.shipping_view, name='shipping'),
    # path('payment/', views.payment_view, name='payment'),
]