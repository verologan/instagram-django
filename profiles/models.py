from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """Perfil de un usuario dentro del Instagram sencillo.

    Un perfil está relacionado 1 a 1 con el usuario autenticado de Django.
    Aquí guardaremos la bio, foto, fecha de nacimiento y más.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField('biografía', blank=True, max_length=500)
    profile_picture = models.ImageField('imagen de perfil', upload_to='profile_pictures/', blank=True, null=True)
    birth_date = models.DateField(verbose_name='Fecha de nacimiento', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Perfil de usuario'
        verbose_name_plural = 'Perfiles de usuario'

    def __str__(self):
        return self.user.username


class Follow(models.Model):
    """Modelo para representar seguidores y seguidos.

    follower = persona que sigue
    followed = persona que recibe el seguimiento
    """

    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['follower', 'followed'], name='unique_follow')
        ]
        verbose_name = 'Seguimiento'
        verbose_name_plural = 'Seguimientos'

    def __str__(self):
        return f'{self.follower} sigue a {self.followed}'
