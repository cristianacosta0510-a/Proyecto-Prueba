from django.contrib import admin
from .models import Curso, Actividad

class CursoAdmin(admin.ModelAdmin):
    # Punto 3.e: Visualizar los campos automáticos (fechas)
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    
    # Opcional: Para ver mejor las columnas en la lista principal
    list_display = ('nombre', 'costo', 'es_presencial', 'fecha_creacion')

admin.site.register(Curso, CursoAdmin)

class ActividadAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion',)
    list_display = ('clave_actividad', 'curso', 'fecha_creacion')
    search_fields = ('clave_actividad', 'curso__nombre')
    list_filter = ('curso', 'fecha_creacion')

admin.site.register(Actividad, ActividadAdmin)
