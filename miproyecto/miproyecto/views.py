from django.http import HttpResponse
from django.shortcuts import render

def pagina_inicio(request):
    #return HttpResponse("Pagina de Inicio")
    return render(request,'inicio.html')

def pagina_acerca_de(request):
    #return HttpResponse("Pagina de Contacto (acerca de)")
    return render(request,'acerca.html')