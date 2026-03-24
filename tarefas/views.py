from django.shortcuts import render
from django.http import JsonResponse
from .models import Tarefas

def listar_tarefas(request):
    tarefas = Tarefas.objects.all().values()
    return JsonResponse(list[any](tarefas), safe=False)

def listar_abertas(request):
    tarefas_abertas = Tarefas.objects.filter(status="ABERTA").values()
    return JsonResponse(list[any](tarefas_abertas), safe=False)