from django.db import models
from datetime import date
class Tarefa(models.Model):
    nome = models.CharField(max_length=40)
    prazo = models.DateField()

    def __str__(self):
        return self.nome

    @property
    def status(self):
        """Retorna se a tarefa está dentro do prazo ou atrasada."""
        if self.prazo < date.today():
            return "Atrasada"
        return "Dentro do prazo"

    class Meta:
        verbose_name_plural = "Tarefas"