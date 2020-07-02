from django.urls import path
from .views import cadastro_user, login_user, render_map


urlpatterns = [
    #path('', index),
    path('cadastro/', cadastro_user, name="CadastroUsuario"),
    path('login/', login_user, name="LoginUsuario"),
    path('rotas/',render_map, name="RendezirarMapa")
    #path('criar/', criar),
    #path('detalhe/<int:id>/', detalhes),
    #path('editar/<int:id>/', editar)
]