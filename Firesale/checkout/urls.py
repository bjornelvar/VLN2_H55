from django.urls import path
from . import views

urlpatterns = [
    # path('', views.checkout_info, name='checkout'),
    path('shipping/', views.shipping_info, name='shipping'),
    path('payment/', views.payment_info, name='payment'),
    path('review/', views.review_info, name='review'),
]