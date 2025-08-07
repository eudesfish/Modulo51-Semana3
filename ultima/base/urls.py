from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inscrever/', views.inscrever, name='inscrever'),
    path('contato/', views.contato, name='contato')
]
