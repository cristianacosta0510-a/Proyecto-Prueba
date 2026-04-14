from django.db import models
from ckeditor.fields import RichTextField

class Curso(models.Model):
    # 1. CharField (Texto corto)
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Curso")
    
    # 2. TextField (Texto largo)
    descripcion = models.TextField(verbose_name="Descripción detallada")
    
    # 3. IntegerField o DecimalField (Números)
    costo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo de Inscripción")
    
    # 4. BooleanField (Booleano)
    es_presencial = models.BooleanField(default=True, verbose_name="¿Es presencial?")

    # 5. CharField (Texto corto)
    instructor = models.CharField(max_length=100, verbose_name="Nombre del Instructor", help_text="Introduce el nombre completo")
    
    # 6. ImageField (Imagen - Requisito explícito)
    # Nota: Recuerda instalar Pillow (pip install Pillow)
    imagen = models.ImageField(upload_to='cursos_img/', verbose_name="Imagen Promocional", null=True, blank=True)
    
    # Fechas de creación y modificación (Requisito explícito)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name="Última Modificación")

    class Meta:
        # Punto 3.b: Nombre de la lista -> Cursos
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        
        # Punto 3.c: Ordenar de más antigua a más reciente
        ordering = ['fecha_creacion'] 

    # Punto 3.f: Permitir visualizar el nombre al registrar (representación del objeto)
    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    # Datos a incluir: clave de la actividad, nombre del curso, descripción de la actividad y fecha de creación.
    clave_actividad = models.CharField(max_length=50, verbose_name="Clave de la Actividad")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nombre del Curso", related_name="actividades")
    descripcion = RichTextField(verbose_name="Descripción de la Actividad")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.clave_actividad} - {self.curso.nombre}"
