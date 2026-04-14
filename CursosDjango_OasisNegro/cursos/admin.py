from django.contrib import admin
from .models import Servicio, Cotizacion, ReporteProblema

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ('nombre', 'descripcion_breve', 'precio_base')
    search_fields = ('nombre', 'descripcion_breve')

admin.site.register(Servicio, ServicioAdmin)

class CotizacionAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_solicitud',)
    list_display = ('nombre_solicitante', 'organizacion', 'servicio_interes', 'fecha_solicitud')
    search_fields = ('nombre_solicitante', 'organizacion', 'email')
    list_filter = ('servicio_interes', 'fecha_solicitud')

admin.site.register(Cotizacion, CotizacionAdmin)

class ReporteProblemaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_reporte',)
    list_display = ('titulo', 'votos', 'fecha_reporte')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('fecha_reporte',)

admin.site.register(ReporteProblema, ReporteProblemaAdmin)
