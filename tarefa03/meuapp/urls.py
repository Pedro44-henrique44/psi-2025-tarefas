from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("usuarios/", views.usuarios, name="usuarios")
]

#para criar um novo "path", uma URL para um nova página, é necessário colocar específicada no inicio: 
#path({colocar aqui, entre aspas}, ... (como está em usuários)
#OBS: se por o nome do arquivo exato ("usuarios.html"; "inicio.html") também funcionará.
#(inclusive eu não sei porque o inicio, que seria o 'index', não precisa disso)