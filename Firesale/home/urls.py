from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home-index'),
    path('search/', views.search_items, name='search-items'),
]