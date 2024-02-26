from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Usuario

@csrf_exempt
def crear_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if 'username' not in data or 'password' not in data:
            return JsonResponse({'error': 'Se requieren el nombre de usuario y la contraseña'}, status=400)
        nuevo_usuario = Usuario(username=data['username'], password=data['password'])
        nuevo_usuario.save()
        return JsonResponse({'mensaje': 'Usuario creado correctamente'}, status=201)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def actualizar_usuario(request, username):
    usuario = Usuario.objects.filter(username=username).first()
    if not usuario:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    
    if request.method == 'PUT':
        data = json.loads(request.body)
        if 'password' not in data:
            return JsonResponse({'error': 'Se requiere la contraseña nueva'}, status=400)
        usuario.password = data['password']
        usuario.save()
        return JsonResponse({'mensaje': 'Contraseña actualizada correctamente'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def borrar_usuario(request, username):
    usuario = Usuario.objects.filter(username=username).first()
    if not usuario:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    
    if request.method == 'DELETE':
        usuario.delete()
        return JsonResponse({'mensaje': 'Usuario eliminado correctamente'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)
