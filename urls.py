from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_caninos, name='listar_caninos'),
    path('agregar/', views.agregar_canino, name='agregar_canino'),
]