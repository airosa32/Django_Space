from django.urls import path
# Views do app sendo importada
from galeria.views import index, imagem



urlpatterns = [
    # "" → rota vazia = página inicial (http://127.0.0.1:8000/)
    # index → função (view) que será executada
    # name="index" → nome da rota para usar no template com {% url 'index' %}
    path("", index, name="index"),

    # "imagem/" → rota que será acessada em /imagem/
    # imagem → função (view) que será executada
    # name="imagem" → nome da rota para usar no template com {% url 'imagem' %}
    path("imagem/", imagem, name="imagem"),
]
