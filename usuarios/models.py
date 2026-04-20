from django.db import models

# Create your models here.
class Usuario(models.Model):
    
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome