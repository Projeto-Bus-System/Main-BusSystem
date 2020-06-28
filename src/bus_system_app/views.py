from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import AlunoForm,UserForm


def cadastro_user(request):
    if request.method == 'POST':
        form_usuario = UserForm(request.POST)
        if form_usuario.is_valid():
 
            form_usuario.save()


            return redirect('cadastro_user')
    else:
        form_usuario = UserForm()
        
    contexto = {
       "form_usuario":form_usuario,
    }
    return render(request, 'cadastro/cadastro.html', contexto)
def login_user(request):
    
    return render(request, 'login/login.html',{})