from django.db import models
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string
from django_resized import ResizedImageField

# Create your models here.
class DiarioMural(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    slug = models.SlugField(max_length=200, default='')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
     # Configuración mejorada con opciones adicionales
    imagen = ResizedImageField(
        size=[300, 300],           # Tamaño máximo
        crop=['middle', 'center'], # Recorta desde el centro (NUEVA)
        quality=75,                # Calidad de compresión
        force_format='WEBP',       # Formato moderno (CAMBIO SUGERIDO)
        keep_meta=False,           # Elimina metadatos (NUEVA)
        upload_to='diario_mural/%Y/%m/',  # Organiza por fecha (NUEVA)
        default='sin_imagen.png',  # Imagen por defecto
        blank=True                 # Campo opcional
    )
    tipo = models.ForeignKey('EstadoDiarioMural', on_delete=models.PROTECT, default=1)
    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo) 
        while DiarioMural.objects.filter(slug=self.slug).exists():
            self.slug += get_random_string(length=4)
        super(DiarioMural, self).save(*args, **kwargs)


class EstadoDiarioMural(models.Model):
    nombre_estado = models.CharField(max_length=30)
    ESTADO_CHOICES = [
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    ]
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='A')

    def __str__(self) -> str:
        return f"{self.nombre_estado} - ({'Activo' if self.estado == 'A' else 'Inactivo'})"