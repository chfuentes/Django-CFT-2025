# miproyecto

Documentación completa del proyecto Django "miproyecto"

Índice
------

- [Resumen](#resumen)
- [Funcionalidades](#funcionalidades)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Dependencias principales](#dependencias-principales)
- [Instalación y ejecución](#instalación-y-ejecución)
- [Desarrollo y comandos comunes](#desarrollo-y-comandos-comunes)
- [Archivos importantes y configuración](#archivos-importantes-y-configuración)
- [Modelos de datos](#modelos-de-datos)
- [APIs y vistas](#apis-y-vistas)
- [Plantillas y frontend](#plantillas-y-frontend)
- [Notas sobre despliegue](#notas-sobre-despliegue)
- [Buenas prácticas y contribución](#buenas-prácticas-y-contribución)

## Resumen

`miproyecto` es una aplicación web completa construida con Django 5.2.8 que implementa un sistema de "Diario Mural" digital. El proyecto permite a los usuarios crear, gestionar y compartir publicaciones con imágenes, organizadas por categorías y estados. Incluye un sistema completo de autenticación de usuarios y una interfaz moderna construida con Bootstrap 5.

El proyecto consta de dos aplicaciones principales:
- **`diariomural`**: Gestión completa del diario mural con CRUD de publicaciones
- **`usuarios`**: Sistema de autenticación y gestión de usuarios

## Funcionalidades

### Gestión de Diario Mural
- ✅ Crear publicaciones con título, contenido y imagen destacada
- ✅ Editar y eliminar publicaciones existentes
- ✅ Listado de publicaciones con filtros por estado/categoría
- ✅ Vista detallada de cada publicación
- ✅ Generación automática de slugs únicos
- ✅ Procesamiento automático de imágenes (redimensionamiento, formato WEBP)
- ✅ Validaciones avanzadas en formularios
- ✅ Mensajes de éxito/error con Django Messages

### Sistema de Usuarios
- ✅ Registro de nuevos usuarios
- ✅ Inicio y cierre de sesión
- ✅ Protección de rutas con decoradores `@login_required`
- ✅ Gestión de sesiones personalizadas
- ✅ Contador de visitas por usuario

### Características Técnicas
- ✅ Interfaz responsive con Bootstrap 5
- ✅ Formularios con django-crispy-forms
- ✅ Manejo de archivos multimedia
- ✅ Base de datos SQLite (desarrollo) / MySQL (producción)
- ✅ Sistema de migraciones completo
- ✅ Configuración de zona horaria (America/Santiago)
- ✅ Internacionalización (LANGUAGE_CODE = 'es')

## Estructura del proyecto

```
miproyecto/
├── db.sqlite3                    # Base de datos SQLite
├── manage.py                     # Comando de gestión Django
├── miproyecto/                   # Configuración del proyecto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              # Configuración principal
│   ├── urls.py                  # URLs del proyecto
│   ├── views.py                 # Vistas generales
│   └── wsgi.py
├── diariomural/                 # App Diario Mural
│   ├── migrations/              # Migraciones de BD
│   ├── templates/diariomural/  # Plantillas HTML
│   ├── __init__.py
│   ├── admin.py                 # Configuración admin
│   ├── apps.py
│   ├── forms.py                 # Formularios ModelForm
│   ├── models.py                # Modelos DiarioMural y EstadoDiarioMural
│   ├── tests.py
│   ├── urls.py                  # URLs de la app
│   └── views.py                 # Vistas CRUD
├── usuarios/                    # App Usuarios
│   ├── templates/usuarios/      # Plantillas login/registro
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                # Modelos de usuario (vacío por ahora)
│   ├── tests.py
│   ├── urls.py                  # URLs de autenticación
│   └── views.py                 # Vistas login/logout/registro
├── media/                       # Archivos subidos por usuarios
├── static/                      # Assets estáticos
│   ├── css/
│   │   ├── base/                # CSS base (reset, variables, animaciones)
│   │   ├── components/          # Componentes (buttons, cards, forms, etc.)
│   │   ├── pages/               # CSS específico por página
│   │   └── estilo.css           # CSS principal
│   ├── js/
│   │   ├── particles.min.js     # Librería de partículas
│   │   └── script.js            # JavaScript personalizado
│   └── ...
├── templates/                   # Plantillas globales
│   ├── layout.html              # Layout base
│   ├── inicio.html              # Página de inicio
│   ├── acerca.html              # Página "Acerca de"
│   └── partials/                # Componentes reutilizables
└── requirements.txt             # Dependencias Python
```

## Dependencias principales

Basado en `requirements.txt`:

- **Django==5.2.8** - Framework web principal
- **django-crispy-forms==2.4** - Renderizado de formularios
- **crispy-bootstrap5==2025.6** - Tema Bootstrap 5 para crispy-forms
- **django-resized==1.0.3** - Procesamiento de imágenes
- **Pillow==12.0.0** - Manipulación de imágenes
- **mysqlclient==2.2.7** - Conector MySQL (para producción)
- **asgiref==3.10.0**, **sqlparse==0.5.3**, **tzdata==2025.2** - Dependencias Django

## Instalación y ejecución

### Prerrequisitos
- Python 3.8+
- Git
- MySQL (solo para producción)
- Entorno virtual (recomendado)

### Pasos de instalación (Windows / PowerShell)

1. **Clonar el repositorio:**
```powershell
git clone <url-del-repositorio>
cd miproyecto
```

2. **Configurar variables de entorno:**
```powershell
# Copiar archivo de ejemplo
copy .env.example .env

# Editar .env con tus valores (ver sección de configuración)
```

3. **Crear y activar entorno virtual:**
```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

4. **Instalar dependencias:**
```powershell
pip install -r requirements.txt
```

5. **Aplicar migraciones:**
```powershell
python miproyecto\manage.py migrate
```

6. **Crear superusuario:**
```powershell
python miproyecto\manage.py createsuperuser
```

7. **Ejecutar servidor de desarrollo:**
```powershell
python miproyecto\manage.py runserver
```

8. **Acceder a la aplicación:**
   - Frontend: `http://127.0.0.1:8000/`
   - Admin: `http://127.0.0.1:8000/admin/`

### Configuración de Entornos

#### Desarrollo (SQLite)
Por defecto, la aplicación usa SQLite. No se requiere configuración adicional.

#### Producción (MySQL)
Para usar MySQL en producción:

1. **Instalar MySQL y crear base de datos:**
```sql
CREATE DATABASE django CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'django_user'@'localhost' IDENTIFIED BY 'tu_password_seguro';
GRANT ALL PRIVILEGES ON django.* TO 'django_user'@'localhost';
FLUSH PRIVILEGES;
```

2. **Configurar variables de entorno en `.env`:**
```env
DJANGO_ENV=production
SECRET_KEY=tu-clave-secreta-muy-segura-aqui
DB_NAME=django
DB_USER=django_user
DB_PASSWORD=tu_password_seguro
DB_HOST=localhost
DB_PORT=3306
ALLOWED_HOSTS=tudominio.com,www.tudominio.com
```

3. **Ejecutar migraciones en producción:**
```powershell
# Asegurarse de que DJANGO_ENV=production esté en .env
python miproyecto\manage.py migrate
```

#### Cambiar entre entornos

**Desarrollo:**
```powershell
# En .env o variable de entorno
DJANGO_ENV=development
# O no definir la variable (usa desarrollo por defecto)
```

**Producción:**
```powershell
# En .env o variable de entorno
DJANGO_ENV=production
```

**Verificar entorno actual:**
```python
# En shell de Django
python miproyecto\manage.py shell
>>> from django.conf import settings
>>> print(settings.ENVIRONMENT)  # 'development' o 'production'
>>> print(settings.DEBUG)        # True (desarrollo) o False (producción)
```

## Desarrollo y comandos comunes

### Comandos Django frecuentes

```powershell
# Crear migraciones para una app específica
python miproyecto\manage.py makemigrations diariomural

# Crear migraciones para todas las apps
python miproyecto\manage.py makemigrations

# Aplicar migraciones
python miproyecto\manage.py migrate

# Crear superusuario
python miproyecto\manage.py createsuperuser

# Ejecutar servidor de desarrollo
python miproyecto\manage.py runserver

# Ejecutar servidor en puerto específico
python miproyecto\manage.py runserver 8080

# Recopilar archivos estáticos
python miproyecto\manage.py collectstatic

# Ejecutar tests
python miproyecto\manage.py test

# Crear nueva app
python miproyecto\manage.py startapp nueva_app
```

### Comandos Git comunes

```powershell
# Ver estado del repositorio
git status

# Añadir cambios
git add .

# Crear commit
git commit -m "Descripción del commit"

# Push a repositorio remoto
git push origin main

# Pull de cambios remotos
git pull origin main
```

## Archivos importantes y configuración

### Configuración Principal (`miproyecto/settings.py`)

**Configuraciones críticas:**
- `DEBUG = True` (solo desarrollo)
- `ALLOWED_HOSTS = []` (configurar para producción)
- `LANGUAGE_CODE = 'es'` (español)
- `TIME_ZONE = 'America/Santiago'`
- Base de datos SQLite para desarrollo
- Configuración de archivos estáticos y media

**Apps instaladas:**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'diariomural',
    'usuarios',
    'crispy_forms',
    'crispy_bootstrap5'
]
```

### URLs del Proyecto (`miproyecto/urls.py`)

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_inicio, name='inicio'),
    path('acerca/', pagina_acerca_de, name='acerca_de'),
    path('diariomural/', include('diariomural.urls')),
    path('usuarios/', include('usuarios.urls'))
]
```

### Gestión de Archivos Estáticos

- **STATIC_URL**: `/static/` - URL para archivos estáticos
- **STATICFILES_DIRS**: `[BASE_DIR / 'static/']` - Directorios de búsqueda
- **MEDIA_URL**: `/media/` - URL para archivos subidos
- **MEDIA_ROOT**: `BASE_DIR / 'media/'` - Directorio de almacenamiento

## Modelos de datos

### DiarioMural (`diariomural/models.py`)

```python
class DiarioMural(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    slug = models.SlugField(max_length=200, default='')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = ResizedImageField(...)  # Imagen procesada automáticamente
    tipo = models.ForeignKey('EstadoDiarioMural', on_delete=models.PROTECT)
```

**Características:**
- Slug automático generado desde el título
- Imagen redimensionada a 300x300px, formato WEBP
- Relación con EstadoDiarioMural

### EstadoDiarioMural

```python
class EstadoDiarioMural(models.Model):
    nombre_estado = models.CharField(max_length=30)
    estado = models.CharField(max_length=1, choices=[('A', 'Activo'), ('I', 'Inactivo')])
```

## APIs y vistas

### Vistas de Diario Mural (`diariomural/views.py`)

- `lista_diariomural()` - Lista todas las publicaciones
- `lista_custom_diariomural()` - Lista con filtros por tipo
- `detalle_diariomural(request, slug)` - Vista detallada
- `crear_diariomural(request)` - Crear nueva publicación
- `editar_diariomural(request, slug)` - Editar publicación existente
- `eliminar_diariomural(request, slug)` - Eliminar publicación

### Vistas de Usuarios (`usuarios/views.py`)

- `vista_registro(request)` - Registro de usuarios (protegido por @login_required)
- `vista_login(request)` - Inicio de sesión
- `vista_logout(request)` - Cierre de sesión

### Vistas Generales (`miproyecto/views.py`)

- `pagina_inicio(request)` - Página principal con contador de visitas
- `pagina_acerca_de(request)` - Página "Acerca de"

## Plantillas y frontend

### Sistema de Plantillas
- **Layout base**: `templates/layout.html` con navegación y estructura común
- **Páginas principales**: `inicio.html`, `acerca.html`
- **Partials**: `partials/` con componentes reutilizables (navbar, footer, head, scripts)

### Framework CSS/JavaScript
- **Bootstrap 5**: Framework CSS responsive
- **django-crispy-forms**: Renderizado automático de formularios
- **JavaScript personalizado**: `static/js/script.js`
- **Partículas animadas**: `particles.min.js` para efectos visuales

### Características de UI/UX
- Diseño moderno con gradientes y efectos de vidrio (backdrop-filter)
- Carrusel hero en página de inicio
- Cards interactivas con hover effects
- Formularios validados con Bootstrap
- Mensajes de feedback con Django Messages
- Responsive design para móviles y desktop

## Notas sobre despliegue

### Configuración para producción

1. **Variables de entorno:**
   - `DEBUG = False`
   - `ALLOWED_HOSTS = ['tu-dominio.com']`
   - Configurar `SECRET_KEY` segura

2. **Base de datos:**
   - Cambiar a PostgreSQL o MySQL
   - Configurar credenciales de BD

3. **Archivos estáticos:**
   - Ejecutar `collectstatic`
   - Configurar servidor web (Nginx/Apache) para servir estáticos

4. **Seguridad:**
   - Configurar HTTPS
   - Usar variables de entorno para secrets
   - Configurar CORS si es necesario

### Servicios de hosting recomendados
- **Heroku** (fácil setup)
- **DigitalOcean** (VPS)
- **AWS/GCP/Azure** (escalable)
- **Railway** (moderno)

## Buenas prácticas y contribución

### Estándares de código
- Seguir PEP 8 para Python
- Usar commits descriptivos en inglés
- Documentar funciones y clases
- Mantener código DRY (Don't Repeat Yourself)

### Contribución
1. Fork el repositorio
2. Crear rama feature: `git checkout -b feature/nueva-funcionalidad`
3. Commit cambios: `git commit -m "Add nueva funcionalidad"`
4. Push a rama: `git push origin feature/nueva-funcionalidad`
5. Crear Pull Request

### Testing
- Ejecutar `python manage.py test` antes de commits
- Probar funcionalidades manualmente
- Verificar responsive design

### Documentación
- Mantener README actualizado
- Documentar nuevas funcionalidades
- Comentar código complejo

---

**Última actualización:** Noviembre 2025
**Versión Django:** 5.2.8
**Estado:** Producción Ready
