from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-index'), # Sækir úr template>home>home-index.html
]