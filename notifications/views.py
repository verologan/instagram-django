from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

from .models import Notification


def notification_list(request, username=None):
    """Vista para listar las notificaciones del usuario.

    Se puede acceder a /notificaciones/ y, si luego quieres,
    filtrar por usuario concreto.
    """
    if username:
        user = get_object_or_404(User, username=username)
        notifications = Notification.objects.filter(user=user)
    else:
        notifications = Notification.objects.all()

    return render(request, 'notifications/notification_list.html', {
        'notifications': notifications,
    })
