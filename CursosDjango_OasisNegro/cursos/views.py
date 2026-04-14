from django.shortcuts import render, redirect, get_object_or_404
from .models import Servicio, ReporteProblema
from .forms import ReporteProblemaForm

# Create your views here.
def registros(request):
    servicios = Servicio.objects.all()  
    return render(request, "cursos/cursos.html", {'servicios': servicios})

def lista_problemas(request):
    problemas = ReporteProblema.objects.all()
    return render(request, "cursos/lista_problemas.html", {'problemas': problemas})

def reportar_problema(request):
    if request.method == 'POST':
        form = ReporteProblemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reportes:lista_problemas')
    else:
        form = ReporteProblemaForm()
    
    return render(request, "cursos/reportar.html", {'form': form})

def votar_problema(request, problema_id):
    problema = get_object_or_404(ReporteProblema, pk=problema_id)
    problema.votos += 1
    problema.save()
    return redirect('reportes:lista_problemas')