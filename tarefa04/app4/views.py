from django.shortcuts import render
from datetime import date
from . models import Tarefa
# context['hoje'] = date.today()

def index(request):
    context = {
        "hoje": date.today(),
        "tarefas": Tarefa.objects.all()
    }
    return render(request, "index.html", context)
# Create your views here.
