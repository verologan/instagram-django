"""Rutas del módulo de perfiles.

Aquí se definen las URLs relacionadas con los usuarios y sus perfiles.
Cada path() conecta una URL con una vista del archivo views.py.
"""

from django.urls import path

from .views import edit_profile, profile_detail, toggle_follow

urlpatterns = [
    # /usuarios/editar/ -> editar perfil del usuario logueado
    path('editar/', edit_profile, name='edit_profile'),
    # /usuarios/ana/ -> perfil público del usuario
    path('<str:username>/', profile_detail, name='profile_detail'),
    # /usuarios/ana/seguir/ -> seguir o dejar de seguir
    path('<str:username>/seguir/', toggle_follow, name='toggle_follow'),
]
