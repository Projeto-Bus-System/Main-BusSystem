from .models import Aluno
from django import forms

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'