# en inicio/views.py
from django.shortcuts import render
from cursos.models import Servicio

def inicio(request):
    servicios = Servicio.objects.all()
    return render(request, 'cursos/cursos.html', {'servicios': servicios})

def nosotros(request):
    return render(request, 'inicio/nosotros.html')

def servicios(request):
    return render(request, 'inicio/servicios.html')

def servicio_vial(request):
    return render(request, 'inicio/servicio_vial.html')
    
def servicio_parques(request):
    return render(request, 'inicio/servicio_parques.html')
    
def servicio_iot(request):
    return render(request, 'inicio/servicio_iot.html')

def blog(request):
    return render(request, 'inicio/blog.html')

def contacto(request):
    return render(request, 'inicio/contacto.html')

def catalogo(request):
    return render(request, 'inicio/catalogo.html')