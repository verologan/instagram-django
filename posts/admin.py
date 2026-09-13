from django.contrib import admin

from .models import Comment, Like, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'caption', 'created_at')
    search_fields = ('author__username', 'caption')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    search_fields = ('author__username', 'text')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    search_fields = ('user__username',)
