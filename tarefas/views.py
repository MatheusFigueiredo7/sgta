from django.shortcuts import render
from django.http import JsonResponse
from .models import Tarefas

def listar_tarefas(request):
    tarefas = Tarefas.objects.values('id', 'titulo', 'descricao', 'status', 'prioridade', 'data_criacao', 'data_entrega', 'usuario_responsavel', 'usuario_responsavel__nome')
    return JsonResponse(list(tarefas), safe=False)

def listar_abertas(request):
    tarefas_abertas = Tarefas.objects.filter(status="ABERTA").values()
    return JsonResponse(list(tarefas_abertas), safe=False)

def listar_prioridade(request, prioridade):
    tarefa_prioridade = Tarefas.objects.filter(prioridade__iexact=prioridade).values()
    if tarefa_prioridade:
        return JsonResponse(list(tarefa_prioridade), safe=False)
    else:
        return JsonResponse({'Erro': f'Nenhuma tarefa encontrada com prioridade {prioridade}.'}, status=404)

def listar_id(request, id):
    tarefa_id = Tarefas.objects.filter(id=id).values()
    if tarefa_id:
        return JsonResponse(list(tarefa_id), safe=False)
    else:
        return JsonResponse({'Erro': f'Nenhuma tarefa encontrada com o ID {id}.'}, status=404)

def listar_aberta_urgente(request):
    tarefas_abertas_urgentes = Tarefas.objects.filter(status="ABERTA", prioridade="URGENTE").values()
    return JsonResponse(list(tarefas_abertas_urgentes), safe=False)

def listar_atrasadas_nao_concluidas(request):
    tarefas_atrasadas_nao_concluidas = Tarefas.objects.exclude(status="CONCLUIDA").filter(data_entrega__lt='2026-04-06').values()
    return JsonResponse(list(tarefas_atrasadas_nao_concluidas), safe=False)

def buscar_tarefas_titulo(request, palavra):
    tarefas_titulo = Tarefas.objects.filter(titulo__icontains=palavra).values()
    return JsonResponse(list(tarefas_titulo), safe=False)
