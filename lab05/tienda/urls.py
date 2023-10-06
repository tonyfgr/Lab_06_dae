from django.urls import path
from . import views

urlpatterns = [
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),
    path('cambiar_precio/', views.cambiar_precio, name='cambiar_precio'),
]
