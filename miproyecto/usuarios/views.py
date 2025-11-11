from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='usuarios:login')
def vista_registro(request):
    if request.method == "POST":
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Usuario se ha creado exitosamente")
            return redirect('diariomural:lista_diariomural')
    else:
        formulario = UserCreationForm()
    return render(request, 'usuarios/registro.html',{'formulario':formulario})

def vista_login(request):
    if request.method == "POST":
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            messages.success(request, f"{usuario} ha iniciado sesion")
            return redirect('diariomural:lista_diariomural')
    else:
        formulario = AuthenticationForm()
    return render(request, 'usuarios/login.html',{'formulario':formulario})  

def vista_logout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Sesion cerrada exitosamente")
        return redirect('diariomural:lista_diariomural')