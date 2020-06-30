from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import AlunoForm,UserForm


def cadastro_user(request):
    if request.method == 'POST':
        form_usuario = UserForm(request.POST)
        form_aluno = AlunoForm(request.POST)
        if form_usuario.is_valid() and form_aluno.is_valid():
            save_form_usuario = form_usuario.save()
            save_form_aluno = form_aluno.save(commit=False)
            save_form_aluno.aluno_usuario = save_form_usuario
            save_form_aluno.save()
            
            return redirect('cadastro_user')
    else:
        form_usuario = UserForm()
        form_aluno = AlunoForm()

        
    contexto = {
       "form_usuario":form_usuario,
       "form_aluno":form_aluno
    }
    return render(request, 'cadastro/cadastro.html', contexto)
def login_user(request):
    
    return render(request, 'login/login.html',{})