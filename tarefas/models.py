from django.db import models

class Tarefas(models.Model):
    status_choices = [
        ("ABERTA", "Aberta"),
        ("EM_ANDAMENTO", "Em andamento"),
        ("CONCLUIDA", "Concluída"),
        ("CANCELADA", "Cancelada")
    ]
    
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=status_choices, default="ABERTA")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()
    prioridade = [
        ("URGENTE", "Urgente"),
        ("NAO_URGENTE", "Não urgente")
    ]
    
    def __str__(self):
        return self.titulo