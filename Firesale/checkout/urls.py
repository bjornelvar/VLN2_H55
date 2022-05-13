from django.urls import path
from .views import CheckoutWizard
from .views import FORMS

urlpatterns = [
    path('<int:id>', CheckoutWizard.as_view(FORMS), name='checkout'),

]