"""Rutas del módulo de posts.

Aquí se definen las URLs relacionadas con publicaciones.
"""

from django.urls import path

from .views import add_comment, create_post, home_feed, post_detail, toggle_like

urlpatterns = [
    # /posts/ -> lista de publicaciones
    path('', home_feed, name='post_feed'),
    # /posts/nueva/ -> crear una publicación
    path('nueva/', create_post, name='create_post'),
    # /posts/5/ -> detalle del post 5
    path('<int:post_id>/', post_detail, name='post_detail'),
    # /posts/5/like/ -> dar o quitar like
    path('<int:post_id>/like/', toggle_like, name='toggle_like'),
    # /posts/5/comentar/ -> añadir comentario
    path('<int:post_id>/comentar/', add_comment, name='add_comment'),
]
