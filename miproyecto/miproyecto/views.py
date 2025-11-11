"""Vistas generales del proyecto `miproyecto`.

Incluye vistas simples para la página de inicio y la página "acerca de".
Estas vistas renderizan plantillas estáticas que forman la portada del sitio.
"""
from django.http import HttpResponse
from django.shortcuts import render


def pagina_inicio(request):
    """Renderiza la página principal del sitio.

    Normalmente muestra la plantilla `inicio.html`. Se dejó un `HttpResponse`
    comentado que puede usarse para pruebas rápidas.
    """
    # return HttpResponse("Pagina de Inicio")
    return render(request, 'inicio.html')


def pagina_acerca_de(request):
    """Renderiza la página "acerca de".

    Muestra información general del proyecto o contacto en `acerca.html`.
    """
    # return HttpResponse("Pagina de Contacto (acerca de)")
    return render(request, 'acerca.html')