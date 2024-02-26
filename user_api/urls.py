from django.urls import path
from . import views

urlpatterns = [
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('actualizar_usuario/<str:username>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('borrar_usuario/<str:username>/', views.borrar_usuario, name='borrar_usuario'),
]
