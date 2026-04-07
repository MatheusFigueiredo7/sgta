from django.urls import path
from .views import listar_tarefas, listar_abertas, listar_prioridade, listar_id, listar_aberta_urgente, listar_atrasadas_nao_concluidas, buscar_tarefas_titulo

urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('tarefas/abertas/', listar_abertas),
    path('tarefas/prioridade/<str:prioridade>', listar_prioridade),
    path('tarefas/<int:id>', listar_id),
    path('tarefas/abertas_urgentes', listar_aberta_urgente),
    path('tarefas/atrasadas_nao_concluidas', listar_atrasadas_nao_concluidas),
    path('tarefas/busca/<str:palavra>/', buscar_tarefas_titulo),
]