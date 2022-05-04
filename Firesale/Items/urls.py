from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='items-index'),
    path('create_listing/', views.create_listing, name='create_listing'),
]