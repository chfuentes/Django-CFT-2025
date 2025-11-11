from django import forms
from .models import DiarioMural
from django.forms import Textarea, TextInput, FileInput, Select
from django.core.exceptions import ValidationError


class CrearDiarioMural(forms.ModelForm):
    """
    Formulario para crear y editar publicaciones del Diario Mural.
    Usa widgets personalizados de Bootstrap 5 para el renderizado.
    Compatible con django-crispy-forms usando el filtro |crispy.
    """
    
    class Meta:
        model = DiarioMural
        
        # Solo incluimos campos editables por el usuario
        # 'slug' y 'fecha_publicacion' se generan automáticamente
        fields = ['titulo', 'contenido', 'imagen', 'tipo']
        
        # Etiquetas personalizadas para mejorar la experiencia del usuario
        # Estas reemplazan los nombres de campo por defecto
        labels = {
            'titulo': 'Título del Diario Mural',
            'contenido': 'Contenido',
            'imagen': 'Imagen Destacada',  # Capitalizado para consistencia
            'tipo': 'Estado/Categoría'
        }
        
        # Textos de ayuda que aparecen debajo de cada campo
        # Proporcionan contexto y orientación al usuario
        help_texts = {
            'titulo': 'Máximo 50 caracteres. Sea descriptivo.',
            'contenido': 'Redacte el contenido completo de la publicación.',  # Actualizado
            'imagen': 'Formato PNG/JPG. Tamaño recomendado: 300x300px. Campo opcional.',  # Especifica formatos
            'tipo': 'Seleccione el estado o categoría del diario mural.'  # Más descriptivo
        }
        
        # Mensajes de error personalizados en español
        # Mejoran la claridad cuando ocurren errores de validación
        error_messages = {
            'titulo': {
                'required': 'El título es obligatorio.',
                'max_length': 'El título no puede exceder los 50 caracteres.'
            },
            'contenido': {
                'required': 'Debe ingresar el contenido del diario mural.'
            },
            'tipo': {
                'required': 'Debe seleccionar un tipo/estado.',
                'invalid_choice': 'Seleccione una opción válida de la lista.'  # Error adicional
            }
        }
        
        # Widgets personalizados con clases Bootstrap 5
        # Controlan cómo se renderiza cada campo en HTML
        widgets = {
            # Campo de texto simple para el título
            'titulo': TextInput(attrs={
                'class': 'form-control',  # Clase Bootstrap para estilos
                'placeholder': 'Ingrese el título aquí...',  # Texto de ayuda visual
                'maxlength': '50',  # Límite de caracteres en el navegador
                'autofocus': True  # El cursor inicia aquí al cargar la página
            }),
            
            # Área de texto para el contenido
            'contenido': Textarea(attrs={
                'style': 'resize:none;',  # Desactiva el redimensionamiento del textarea
                'placeholder': 'Ingrese el contenido del diario mural aquí...',
                'class': 'form-control',  # Clase Bootstrap para estilos
                'rows': 6  # Define la altura inicial del textarea
            }),
            
            # Campo de archivo para subir imágenes
            'imagen': FileInput(attrs={
                'class': 'form-control',  # Clase Bootstrap 5 para inputs de archivo
                'accept': 'image/png,image/jpeg,image/jpg'  # Limita tipos de archivo seleccionables
            }),
            
            # Select dropdown para elegir el tipo/estado
            'tipo': Select(attrs={
                'class': 'form-select'  # Bootstrap 5 usa 'form-select' para <select>
            })
        }
    
    # VALIDACIONES PERSONALIZADAS
    # Django ejecuta estos métodos automáticamente durante form.is_valid()
    
    def clean_titulo(self):
        """
        Validación personalizada para el campo 'titulo'.
        - Verifica longitud mínima (5 caracteres)
        - Previene títulos completamente en mayúsculas
        - Elimina espacios en blanco al inicio y final
        """
        titulo = self.cleaned_data.get('titulo')
        
        if titulo:
            # Limpiar espacios en blanco
            titulo = titulo.strip()
            
            # Validar longitud mínima para títulos significativos
            if len(titulo) < 5:
                raise ValidationError(
                    'El título debe tener al menos 5 caracteres.'
                )
            
            # Evitar títulos completamente en mayúsculas (mala práctica)
            # Solo valida si el título tiene más de 10 caracteres
            if titulo.isupper() and len(titulo) > 10:
                raise ValidationError(
                    'Evite escribir todo el título en mayúsculas.'
                )
            
            # VALIDACIÓN ADICIONAL: Prevenir títulos duplicados
            # Busca si ya existe un título igual (ignorando mayúsculas/minúsculas)
            qs = DiarioMural.objects.filter(titulo__iexact=titulo)
            
            # Si estamos editando, excluir el registro actual de la búsqueda
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            
            # Si encuentra duplicados, lanzar error
            if qs.exists():
                raise ValidationError(
                    'Ya existe un diario mural con este título. '
                    'Por favor, elija uno diferente.'
                )
        
        return titulo  # Retornar el valor limpio
    
    def clean_contenido(self):
        """
        Validación personalizada para el campo 'contenido'.
        - Verifica longitud mínima (20 caracteres)
        - Elimina espacios en blanco al inicio y final
        """
        contenido = self.cleaned_data.get('contenido')
        
        if contenido:
            # Limpiar espacios en blanco
            contenido = contenido.strip()
            
            # Validar longitud mínima para contenido significativo
            if len(contenido) < 20:
                raise ValidationError(
                    'El contenido debe tener al menos 20 caracteres.'
                )
        
        return contenido  # Retornar el valor limpio
    
    def clean_imagen(self):
        """
        Validación personalizada para el campo 'imagen'.
        - Verifica tamaño máximo de archivo (5MB)
        - Valida extensiones permitidas (png, jpg, jpeg)
        - Proporciona mensajes de error detallados
        """
        imagen = self.cleaned_data.get('imagen')
        
        # Solo validar si se subió una imagen
        # hasattr verifica que el objeto tenga el atributo 'size'
        if imagen and hasattr(imagen, 'size'):
            
            # Validar tamaño máximo de archivo
            max_size = 5 * 1024 * 1024  # 5MB en bytes (5 * 1024KB * 1024bytes)
            
            if imagen.size > max_size:
                # Calcular tamaño actual en MB para el mensaje
                size_mb = round(imagen.size / (1024 * 1024), 2)
                raise ValidationError(
                    f'La imagen no puede superar los 5MB. '
                    f'Tamaño actual: {size_mb}MB.'
                )
            
            # Validar extensión del archivo
            valid_extensions = ['png', 'jpg', 'jpeg']
            
            # Extraer extensión del nombre del archivo
            ext = imagen.name.split('.')[-1].lower()
            
            if ext not in valid_extensions:
                raise ValidationError(
                    f'Formato de imagen no válido. '
                    f'Use: {", ".join(valid_extensions).upper()}.'
                )
        
        return imagen  # Retornar el valor validado
