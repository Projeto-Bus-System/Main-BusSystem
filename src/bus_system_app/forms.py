from .models import Aluno
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','email']

       