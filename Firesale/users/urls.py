from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView)
from django.urls import reverse_lazy
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile_edit', views.edit_profile, name='profile-edit'),
    path('profile', views.show_profile, name='profile'),
    path('my_listings/', views.my_listings, name='my-listings'),
    path('my_bids', views.my_bids, name='my-bids'),
    path('', views.accept_bid, name='accept-bid'),
    path('my_listings/edit_listing/<int:id>', views.edit_listing, name='edit-listing'),
    path('my_listings/delete_item/<int:id>', views.delete_item, name='delete-item'),
    path('profile/<int:id>', views.show_profile, name='user-profile'),
    path('my_orders', views.my_orders, name='my-orders'),
    path('profile/settings', views.user_settings, name='user-settings'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='users/password_reset.html',
        email_template_name='users/password_reset_email.html',
        subject_template_name='users/password_reset_subject.txt',
        success_url='/users/password_reset/done/'),
        name='password_reset'
    ),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
        name='password_reset_done'
    ),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html',
        success_url='/users/reset/done/'),
        name='password_reset_confirm'
    ),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
        name='password_reset_complete'
    ),
    path('password_change/', PasswordChangeView.as_view(
        template_name='users/password_change.html',
        success_url=reverse_lazy('password_change_done')),
        name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'),
        name='password_change_done'),
    path('profile/toggle_notifs/', views.toggle_notifications, name='toggle-notifs'),
    path('email_verify/', views.send_email_verify_email, name='email-verify'),
    path('email_verify/<uidb64>/', views.verify_email, name='email-verify-confirm'),
]