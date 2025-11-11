from django.urls import path
from . import views

app_name="diariomural"

urlpatterns = [
    path('', views.lista_diariomural, name='lista_diariomural'),
    path('crear',views.crear_diariomural,name="crear_diariomural"),
    path('<slug:slug>/', views.detalle_diariomural, name='detalle_diariomural')
]
