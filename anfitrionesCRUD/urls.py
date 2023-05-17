from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'anfitrionesCRUD'

urlpatterns = [
    path('', views.lista_anfitriones, name='lista_anfitriones'),
    path('agregar/', views.agregar_anfitrion, name='agregar'),
    path('modificar/<int:anfitrion_id>/', views.modificar_anfitrion, name='modificar'),
    path('eliminar/<int:anfitrion_id>/', views.eliminar_anfitrion, name='eliminar'),
]