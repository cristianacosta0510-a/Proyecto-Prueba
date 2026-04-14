from django import forms
from .models import ReporteProblema

class ReporteProblemaForm(forms.ModelForm):
    class Meta:
        model = ReporteProblema
        fields = ['titulo', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Baches en Zona Sur'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe el problema con detalle...'}),
        }
