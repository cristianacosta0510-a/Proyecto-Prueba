from django.shortcuts import render
from .models import Curso  # 1. Cambiamos Alumnos por Curso

# Create your views here.
def registros(request):
    cursos = Curso.objects.all()  # 2. Consultamos el modelo Curso
    
    # 3. Enviamos los datos al template bajo el nombre 'cursos'
    return render(request, "cursos/cursos.html", {'cursos': cursos})