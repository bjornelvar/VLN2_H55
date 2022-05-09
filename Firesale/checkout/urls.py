from django.urls import path
from . import views

urlpatterns = [
    path('shipping', views.shipping_info, name='checkout'),
    path('billing', views.billing_info, name='checkout'),
    # path('payment', views.PaymentForm, name='checkout'),
    # path('review', views.ReviewForm, name='review'),
]