from django.shortcuts import render, HttpResponse



def cadastro_user(request):
    
    return render(request, 'cadastro/cadastro.html',{})