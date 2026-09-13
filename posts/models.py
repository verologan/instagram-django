from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Publicación del feed tipo Instagram.

    Cada post tiene un autor, texto descriptivo y una imagen opcional.
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    caption = models.CharField('descripción', max_length=2200, blank=True)
    image = models.ImageField('imagen', upload_to='posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return f'Post de {self.author.username}'


class Comment(models.Model):
    """Comentario que un usuario deja en un post."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField('comentario', max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return f'{self.author.username} comentó en {self.post_id}'


class Like(models.Model):
    """Like de un usuario sobre una publicación."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['post', 'user'], name='unique_like_per_user_post')
        ]
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return f'{self.user.username} likes {self.post_id}'
