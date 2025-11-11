"""Vistas de la aplicación `diariomural`.

Contiene las vistas para listar publicaciones, ver detalles y crear nuevas
entradas del diario mural. Las vistas usan el modelo `DiarioMural` y el
formulario `CrearDiarioMural` definido en `forms.py`.
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from diariomural.models import DiarioMural
from django.http import HttpResponse
from . import forms


def lista_diariomural(request):
    """Obtiene y muestra todas las publicaciones del Diario Mural.

    Contexto devuelto a la plantilla:
    - 'diariosmurales': queryset con todas las entradas.
    """
    diariosmurales = DiarioMural.objects.all()
    return render(request, 'diariomural/lista_diariomural.html', {'diariosmurales': diariosmurales})


def detalle_diariomural(request, slug):
    """Muestra el detalle de una publicación identificada por su `slug`.

    Lanza `DoesNotExist` si no se encuentra el objeto; podría envolverse en
    un `try/except` o usar `get_object_or_404` según preferencia.
    """
    detalle_diariomural = DiarioMural.objects.get(slug=slug)
    return render(request, 'diariomural/detalle_diariomural.html', {'detalle_diariomural': detalle_diariomural})


def crear_diariomural(request):
    """Permite crear una nueva entrada del Diario Mural via formulario.

    - Si el método es POST, valida y guarda el formulario incluyendo archivos
      subidos (request.FILES). Al crear con éxito muestra un mensaje y
      redirige a la lista de publicaciones.
    - Si es GET, muestra el formulario vacío.
    """
    if request.method == "POST":
        formulario = forms.CrearDiarioMural(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Publicacion creada exitosamente")
            return redirect('diariomural:lista_diariomural')
    else:
        formulario = forms.CrearDiarioMural()
    return render(request, 'diariomural/crear_diariomural.html', {'formulario': formulario})