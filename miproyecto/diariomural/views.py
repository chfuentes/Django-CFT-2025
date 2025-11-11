from django.shortcuts import render, redirect
from django.contrib import messages
from diariomural.models import DiarioMural
from django.http import HttpResponse
from . import forms

# Create your views here.
def lista_diariomural(request):
    diariosmurales = DiarioMural.objects.all()
    return render(request,'diariomural/lista_diariomural.html',{'diariosmurales':diariosmurales})

def detalle_diariomural(request,slug):
    detalle_diariomural = DiarioMural.objects.get(slug=slug)
    return render(request,'diariomural/detalle_diariomural.html',{'detalle_diariomural':detalle_diariomural})

def crear_diariomural(request):
    if request.method == "POST":
        formulario = forms.CrearDiarioMural(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Publicacion creada exitosamente")
            return redirect('diariomural:lista_diariomural')
    else:
        formulario = forms.CrearDiarioMural()
    return render(request,'diariomural/crear_diariomural.html',{'formulario':formulario})