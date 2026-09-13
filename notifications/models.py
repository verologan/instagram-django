from django.contrib.auth.models import User
from django.db import models


class Notification(models.Model):
    """Notificación del tipo Instagram.

    Se usa para avisar al usuario cuando alguien le sigue, comenta o da like.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField('mensaje', max_length=255)
    link = models.CharField('enlace', max_length=255, blank=True, default='')
    is_read = models.BooleanField('leída', default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'

    def __str__(self):
        return f'{self.user.username}: {self.message}'
