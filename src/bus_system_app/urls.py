from django.urls import path
from .views import cadastro_user


urlpatterns = [
    #path('', index),
    path('cadastro/', cadastro_user, name="CadastroDeUsuario")
    #path('criar/', criar),
    #path('detalhe/<int:id>/', detalhes),
    #path('editar/<int:id>/', editar)
]