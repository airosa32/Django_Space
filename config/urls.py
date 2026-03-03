from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path("admin/", admin.site.urls),
    # Adiciona as rotas dos apps aqui.
    # Cada rota de app aqui é um conjunto de 
    # rotas daquela aplicação.
    path("", include("galeria.urls")),   
]
