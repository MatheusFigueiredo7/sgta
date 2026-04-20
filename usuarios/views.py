from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.
def listar_usuarios(request):
    usuarios = Usuario.objects.all().values()
    return JsonResponse(list(usuarios), safe=False)

def buscar_usuario_por_id(request, id):
    usuario_id = Usuario.objects.filter(id=id).values()
    if not usuario_id:
        return JsonResponse({'error' : f'Erro 404: Usuário de ID {id} inexistente.'}, status=404)
    else:
        return JsonResponse(list(usuario_id), safe=False)