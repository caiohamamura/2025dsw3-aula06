from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('controle/', views.controle, name='lista'),
    path('postar/', views.postar, name='postar'),
]
