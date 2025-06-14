from django.shortcuts import render


def inicio(request):
    return render(request, "inicio.html")

#aqui é onde é colocado oque a página necessitará. 
#escrito no slide: Recebem e processam as requisições, retornando um conteúdo baseado nos templates