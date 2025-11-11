"""Ruteo de la aplicación `usuarios`.

Aquí se definen las rutas relacionadas con la autenticación y gestión de
usuarios (registro, login y logout). Se emplean vistas definidas en
`usuarios.views`.
"""
from django.urls import path
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('registro', views.vista_registro, name='registro'),
    path('login', views.vista_login, name='login'),
    path('logout', views.vista_logout, name="logout")
]
