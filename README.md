# miproyecto

Documentación del proyecto Django "miproyecto"

Índice
------

- Resumen
- Funcionalidades
- Estructura del proyecto
- Dependencias principales
- Instalación y ejecución (Windows / PowerShell)
- Desarrollo y comandos comunes
- Archivos importantes y explicación
- Notas sobre despliegue
- Buenas prácticas y contribución

Resumen
-------

`miproyecto` es una aplicación web construida con Django que incluye al menos dos aplicaciones locales: `diariomural` y `usuarios`.
El proyecto está pensado para gestionar contenido (probablemente un muro o diario mural con imágenes y estados) y autenticación/gestión de usuarios.

Funcionalidades (observadas en el código)
---------------------------------------

- Gestión de usuarios (app `usuarios`): formulario de login, vistas y rutas.
- Módulo `diariomural`: modelos y migraciones para entradas del diario/mural, campos de imagen y estado, manejo de slugs.
- Soporte para subida de imágenes en `media/diario_mural/` (ya existe una carpeta `media/diario_mural/2025/`).
- Uso de `django-crispy-forms` con `crispy_bootstrap5` para renderizar formularios con Bootstrap.

Estructura principal del repositorio
-----------------------------------

- `miproyecto/` — carpeta del proyecto Django (contiene `settings.py`, `urls.py`, `wsgi.py`, etc.).
- `miproyecto/manage.py` — comando de gestión de Django.
- `diariomural/` — app local (modelos, vistas, templates, migrations).
- `usuarios/` — app local (login, templates, vistas, forms).
- `media/` — archivos subidos por usuarios (no debe subirse a GitHub).
- `static/` — assets públicos (css, js).
- `env/` — entorno virtual (ya presente; está ignorado por `.gitignore`).
- `requirements.txt` — dependencias del proyecto (generado con `pip freeze`).

Dependencias principales
------------------------

Basado en los paquetes que aparecen en `env/Lib/site-packages/` y el uso dentro de templates:

- Django (versión ~5.x según los *dist-info* presentes)
- django-crispy-forms
- crispy-bootstrap5
- pillow
- django-resized
- tzdata, asgiref, sqlparse (dependencias típicas)

Instalación y ejecución (Windows / PowerShell)
--------------------------------------------

1. Crear y activar un entorno virtual (si aún no existe). En PowerShell:

```powershell
python -m venv env
; .\env\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
pip install -r .\requirements.txt
```

3. Aplicar migraciones:

```powershell
python .\miproyecto\manage.py migrate
```

4. Crear un superusuario (opcional, para acceder al admin):

```powershell
python .\miproyecto\manage.py createsuperuser
```

5. Ejecutar el servidor de desarrollo:

```powershell
python .\miproyecto\manage.py runserver
```

6. Acceder a la web en `http://127.0.0.1:8000/`.

Desarrollo y comandos útiles
---------------------------

- Ejecutar pruebas (si hay tests):

```powershell
python .\miproyecto\manage.py test
```

- Crear migraciones para una app determinada:

```powershell
python .\miproyecto\manage.py makemigrations nombre_app
```

- Recopilar archivos estáticos (útil para despliegue):

```powershell
python .\miproyecto\manage.py collectstatic
```

Archivos y configuraciones clave
-------------------------------

- `miproyecto/settings.py` — revisa estas áreas importantes:
  - `DEBUG` — dejar `True` solo en desarrollo.
  - `ALLOWED_HOSTS` — configurar para producción.
  - `DATABASES` — actualmente SQLite (`db.sqlite3`) para desarrollo.
  - `STATIC_URL`, `STATIC_ROOT` y `STATICFILES_DIRS` — servir recursos estáticos.
  - `MEDIA_URL`, `MEDIA_ROOT` — servir archivos subidos (`media/`).
  - `INSTALLED_APPS` debe incluir `crispy_forms` y `crispy_bootstrap5`.

- `miproyecto/urls.py` — punto de entrada de rutas; incluye rutas de apps `usuarios` y `diariomural`.

- `usuarios/templates/usuarios/login.html` — plantilla de login (usa Bootstrap y crispy-forms). Se colocó la tarjeta centrada para ocupar ~40% usando grid (`col-md-5`).

- `media/` — carpeta con uploads; ya incluida en `.gitignore` y no se debe subir al repositorio.

Consideraciones de seguridad
----------------------------

- Nunca subir el `.env` ni archivos con claves. Usar variables de entorno para `SECRET_KEY`, credenciales de DB y configuración sensible.
- En producción, establecer `DEBUG = False` y configurar `ALLOWED_HOSTS` apropiadamente.

Despliegue (resumen)
--------------------

1. Preparar settings para producción (usar `django-environ` o variables de entorno).
2. Configurar una base de datos de producción (PostgreSQL, MySQL, etc.).
3. Usar un servidor WSGI/ASGI (Gunicorn / Daphne / uWSGI) detrás de Nginx o IIS.
4. Configurar almacenamiento de archivos (S3 u otro) para media en producción.
5. Ejecutar `collectstatic` y configurar Nginx para servir `STATIC_ROOT` y `MEDIA_ROOT`.

Contribución
------------

- Mantener las migraciones versionadas (no ignorar `migrations/`).
- Ramas: usar ramas descriptivas y pull requests para cambios grandes.
- Añadir tests para nuevas funcionalidades.

Licencia
--------

Incluye aquí la licencia del proyecto (por ejemplo MIT) o un fichero `LICENSE` si corresponde.

Notas finales y próximas mejoras sugeridas
----------------------------------------

- Añadir instrucciones para ejecutar linters (flake8/black) y pre-commit hooks.
- Añadir un `Procfile` o ejemplos de configuración para despliegue en Heroku/Render/Vercel si fuera necesario.
- Incluir `docker-compose.yml` si se desea contenerizar la aplicación para desarrollo y despliegue.

Contacto
--------

Indica aquí el autor o responsable del proyecto y el canal de comunicación (email/issue tracker).
