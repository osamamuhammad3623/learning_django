from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_response, name='home_response'),
]