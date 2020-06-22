from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def cadastro_user(request):
    if request.method == 'POST':
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('cadastro_user')
    else:
        form_usuario = UserCreationForm()

    return render(request, 'cadastro/cadastro.html', {"form_usuario":form_usuario })




#def cadastro_user(request):
    
#    return render(request, 'cadastro/cadastro.html',{})


def login_user(request):
    
    return render(request, 'login/login.html',{})