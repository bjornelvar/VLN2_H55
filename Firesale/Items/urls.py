from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='items-index'),
    path('create_listing/', views.create_listing, name='create_listing'),
    path('<int:id>', views.get_item_by_id, name='items-details'),
    path('search/', views.search_items, name='search-items'),
    path('category/<int:id>', views.get_items_by_category, name='category-items'),
]