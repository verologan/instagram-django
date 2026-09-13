"""Rutas del módulo de notificaciones."""

from django.urls import path

from .views import notification_list

urlpatterns = [
    # Ejemplo: /notificaciones/ => todas las notificaciones
    path('', notification_list, name='notification_list'),
    # Ejemplo: /notificaciones/usuario/ana/ => notificaciones del usuario Ana
    path('usuario/<str:username>/', notification_list, name='user_notifications'),
]
