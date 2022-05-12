from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile_edit', views.edit_profile, name='profile-edit'),
    path('profile', views.show_profile, name='profile'),
    path('my_listings', views.my_listings, name='my-listings'),
    path('my_bids', views.my_bids, name='my-bids'),
    path('', views.accept_bid, name='accept-bid'),
    path('my_listings/edit_listing/<int:id>', views.edit_listing, name='edit-listing'),
    path('profile/<int:id>', views.show_profile, name='user-profile')
]