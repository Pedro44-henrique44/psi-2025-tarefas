from django.shortcuts import render

def inicio(request):
    return render(request, "inicio.html")

def usuarios(request):
    user_list = [
        {"nome": "Diego", "idade": "30", "cidade": "Natal", "matricula": "20101001110029"},
        {"nome": "Pedro", "idade": "17", "cidade": "SPP", "matricula": "20231181110004"},
        {"nome": "Chico", "idade": "21", "cidade": "Natal", "matricula": "20201181110023"},
        {"nome": "Dede", "idade": "27", "cidade": "Natal", "matricula": "20161181110031"},
        {"nome": "Xuao", "idade": "56", "cidade": "Natal", "matricula": "19991181110001"},
    ]

    context = {
        "usuarios": user_list,# "{qualquer nome}": {atributo que você deseja dar como reposta}. isso é um dicionário
    }
    return render(request, "usuarios.html", context)

#aqui é onde é colocado oque a página necessitará. 
#escrito no slide: Recebem e processam as requisições, retornando um conteúdo baseado nos templates
#lembrar de também mudar o nome da função!!!!!!!!!!!!!!!!!