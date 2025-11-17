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
    if request.user.is_authenticated:
        nombre_usuario = request.user.username
        request.session['nombre_usuario'] = nombre_usuario
        if 'visitas' in request.session:
            request.session['visitas'] += 1
        else:
            request.session['visitas'] = 1
        visitas = request.session['visitas']
        mensaje_bienvenida = f"Bienvenido {nombre_usuario}. Has visitado esta página {visitas} veces."
    else:
        mensaje_bienvenida = "Bienvenido visitante. Por favor, inicia sesión para una experiencia personalizada."
    return render(request,'inicio.html', {'mensaje_bienvenida': mensaje_bienvenida})


def pagina_acerca_de(request):
    """Renderiza la página "acerca de".

    Muestra información general del proyecto o contacto en `acerca.html`.
    """
    # return HttpResponse("Pagina de Contacto (acerca de)")
    if 'nombre_usuario' not in request.session:
        request.session['nombre_usuario'] = 'Visitante Anónimo'
    nombre = request.session['nombre_usuario']
    return render(request,'acerca.html',{'nombre_usuario': nombre})