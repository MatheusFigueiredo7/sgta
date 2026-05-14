from django.urls import path
from .views import *

urlpatterns = [
    path('usuarios/', listar_usuarios),
    path('usuarios/<int:id>/', buscar_usuario_por_id)
]