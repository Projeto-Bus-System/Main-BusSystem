from django import forms
from accounts.models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class FormCreateStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['matricula','ponto','telefone','telefone_responsavel']
        

class FromCreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1', 'password2','email']
