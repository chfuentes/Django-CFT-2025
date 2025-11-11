from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='usuarios:login')
def vista_registro(request):
        """
        Vista para crear (registrar) nuevos usuarios.

        Comportamiento:
        - Esta vista está protegida por `login_required`, por lo que solo usuarios
            autenticados pueden acceder a ella; si no están autenticados se redirige
            a la URL con nombre 'usuarios:login'.
            Nota: en muchos proyectos el registro se permite a usuarios anónimos;
            aquí se conserva el decorador existende y por tanto la protección.
        - Si la petición es POST, se instancia `UserCreationForm` con los datos
            enviados, se valida y se guarda el nuevo usuario. Se muestra un mensaje
            de éxito y se redirige a 'diariomural:lista_diariomural'.
        - Si la petición no es POST (p. ej. GET), se muestra el formulario vacío.

        Parámetros:
        - request: HttpRequest (puede contener datos POST con campos del form)

        Retorna:
        - HttpResponse con la plantilla 'usuarios/registro.html' y el contexto
            {'formulario': formulario}
        """
        if request.method == "POST":
                # Cargar el formulario con los datos enviados por POST
                formulario = UserCreationForm(request.POST)
                if formulario.is_valid():
                        # Guardar el nuevo usuario en la base de datos
                        formulario.save()
                        # Mensaje flash para mostrar en la siguiente vista
                        messages.success(request, "Usuario se ha creado exitosamente")
                        # Redirigir a la lista principal del diariomural
                        return redirect('diariomural:lista_diariomural')
        else:
                # Petición GET: crear un formulario vacío para mostrar al usuario
                formulario = UserCreationForm()
        # Renderizar la plantilla con el formulario (ya sea vacío o con errores)
        return render(request, 'usuarios/registro.html', {'formulario': formulario})

def vista_login(request):
        """
        Vista para autenticar (iniciar sesión) a un usuario.

        Comportamiento:
        - Si la petición es POST, se instancia `AuthenticationForm` con los datos
            recibidos. Si es válida, se obtiene el usuario con `get_user()` y se
            llama a `login(request, usuario)` para establecer la sesión.
        - Al iniciar sesión correctamente se añade un mensaje de éxito y se
            redirige a 'diariomural:lista_diariomural'.
        - Si la petición es GET, se muestra el formulario de autenticación vacío.

        Observaciones:
        - `AuthenticationForm` maneja la validación de credenciales y añade
            errores al propio formulario cuando falla la autenticación.
        """
        if request.method == "POST":
                # AuthenticationForm espera los datos 'username' y 'password'
                formulario = AuthenticationForm(data=request.POST)
                if formulario.is_valid():
                        # Obtener la instancia de usuario autenticado
                        usuario = formulario.get_user()
                        # Establecer la sesión del usuario
                        login(request, usuario)
                        messages.success(request, f"{usuario} ha iniciado sesion")
                        return redirect('diariomural:lista_diariomural')
        else:
                # Mostrar el formulario de login vacío
                formulario = AuthenticationForm()
        return render(request, 'usuarios/login.html', {'formulario': formulario})  

def vista_logout(request):
        """
        Vista para cerrar la sesión del usuario.

        - Se espera una petición POST para realizar el logout (mejor práctica para
            evitar cierres de sesión por enlaces GET accidentales o CSRF).
        - Al cerrar sesión se añade un mensaje y se redirige a la lista del
            diariomural.
        """
        if request.method == "POST":
                # Cerrar la sesión del usuario actual
                logout(request)
                messages.success(request, "Sesion cerrada exitosamente")
                return redirect('diariomural:lista_diariomural')