# en inicio/views.py
from django.shortcuts import render
from cursos.models import Curso

def inicio(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/cursos.html', {'cursos': cursos})