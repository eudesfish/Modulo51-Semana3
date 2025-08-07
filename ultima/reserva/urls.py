from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserva_pet, name="reserva_pet"),
]