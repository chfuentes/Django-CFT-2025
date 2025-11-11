"""Rutas de la aplicación `diariomural`.

Contiene las URL para listar, crear y ver detalles de las publicaciones del
diario mural. Las vistas se importan desde el módulo local `views`.
"""
from django.urls import path
from . import views

app_name = "diariomural"

urlpatterns = [
    path('', views.lista_diariomural, name='lista_diariomural'),
    path('crear', views.crear_diariomural, name="crear_diariomural"),
    path('<slug:slug>/', views.detalle_diariomural, name='detalle_diariomural')
]
