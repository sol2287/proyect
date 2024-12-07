from django import forms
from mi_animal.models import Caninos

class CaninoForm(forms.ModelForm):
    class Meta:
        model = Caninos
        fields = ['nombre', 'raza', 'color', 'edad', 'fecha']