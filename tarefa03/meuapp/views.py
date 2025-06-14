from django.shortcuts import render

def inicio(request):
    return render(request, "inicio.html")

def usuarios(request):
    user_list = [
        {"nome": "Diego", "idade": "30", "cidade": "Natal", "matricula": "19451945"},
        {"nome": "Diego", "idade": "30", "cidade": "Natal", "matricula": "19451945"},
        {"nome": "Diego", "idade": "30", "cidade": "Natal", "matricula": "19451945"},
        {"nome": "Diego", "idade": "30", "cidade": "Natal", "matricula": "19451945"},
        {"nome": "Diego", "idade": "30", "cidade": "Natal", "matricula": "19451945"},
    ]

    context = {
        "usuarios": user_list,# "{qualquer nome}": {atributo que você deseja dar como reposta}. isso é um dicionário
    }
    return render(request, "usuarios.html", context)

#aqui é onde é colocado oque a página necessitará. 
#escrito no slide: Recebem e processam as requisições, retornando um conteúdo baseado nos templates
#lembrar de também mudar o nome da função!!!!!!!!!!!!!!!!!