"""Configuración principal de URLs del proyecto.

Aquí se conectan todas las rutas del sitio.
Cada path() indica una URL pública y la relaciona con una vista.
"""

from django.contrib import admin
from django.urls import include, path

from posts.views import home_feed
from profiles.views import register_view

urlpatterns = [
    # Ruta principal del sitio.
    path('', home_feed, name='home'),

    # Panel de administración.
    path('admin/', admin.site.urls),

    # Login y registro de usuarios.
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', register_view, name='register'),

    # Rutas del perfil.
    path('usuarios/', include('profiles.urls')),

    # Rutas de publicaciones.
    path('posts/', include('posts.urls')),

    # Rutas de notificaciones.
    path('notificaciones/', include('notifications.urls')),
]
