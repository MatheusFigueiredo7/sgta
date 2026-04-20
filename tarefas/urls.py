from django.urls import path
from .views import *
urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('tarefas/abertas/', listar_abertas),
    path('tarefas/prioridade/<str:prioridade>/', listar_prioridade),
    path('tarefas/<int:id>/', listar_id),
    path('tarefas/abertas_urgentes/', listar_aberta_urgente),
    path('tarefas/atrasadas_nao_concluidas/', listar_atrasadas_nao_concluidas),
    path('tarefas/busca/<str:palavra>/', buscar_tarefas_titulo),
]