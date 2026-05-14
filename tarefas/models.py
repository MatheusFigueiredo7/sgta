from django.db import models
from usuarios.models import Usuario

class Tarefa(models.Model):
    status_choices = [
        ("ABERTA", "Aberta"),
        ("EM_ANDAMENTO", "Em andamento"),
        ("CONCLUIDA", "Concluída"),
        ("CANCELADA", "Cancelada")
    ]
    prioridades_choices = [
        ("URGENTE", "Urgente"),
        ("NAO_URGENTE", "Não urgente")
    ]
    
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=status_choices, default="ABERTA")
    prioridade = models.CharField(max_length=20, choices=prioridades_choices, default="NAO_URGENTE")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()
    usuario_responsavel = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.titulo