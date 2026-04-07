from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Tarefas

def listar_tarefas(request):
    tarefas = Tarefas.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)

def listar_abertas(request):
    tarefas_abertas = Tarefas.objects.filter(status="ABERTA").values()
    return JsonResponse(list(tarefas_abertas), safe=False)

def listar_prioridade(request, prioridade):
    prioridade_upper = prioridade.upper()

    prioridades_choices = [choice[0] for choice in Tarefas.prioridades_choices]

    if prioridade_upper not in prioridades_choices:
        return JsonResponse({'Erro': 'Prioridade inválida. Opções válidas: Urgente ou Nao_urgente.'}, status=404)

    tarefas_prioritarias = Tarefas.objects.filter(prioridade=prioridade_upper).values()
    return JsonResponse(list(tarefas_prioritarias), safe=False)

def listar_id(request, id):
    try:
        tarefa = Tarefas.objects.get(id=id)
        return JsonResponse(model_to_dict(tarefa))
    except Tarefas.DoesNotExist:
        return JsonResponse({'Erro': f'Tarefa com ID {id} inexistente.'}, status=404)

def listar_aberta_urgente(request):
    tarefas_abertas_urgentes = Tarefas.objects.filter(status="ABERTA", prioridade="URGENTE").values()
    return JsonResponse(list(tarefas_abertas_urgentes), safe=False)

def listar_atrasadas_nao_concluidas(request):
    tarefas_atrasadas_nao_concluidas = Tarefas.objects.exclude(status="CONCLUIDAS").filter(data_entrega__lt='2026-04-06').values()
    return JsonResponse(list(tarefas_atrasadas_nao_concluidas), safe=False)

def buscar_tarefas_titulo(request, palavra):
    tarefas_titulo = Tarefas.objects.filter(titulo__icontains=palavra).values()
    return JsonResponse(list(tarefas_titulo), safe=False)
