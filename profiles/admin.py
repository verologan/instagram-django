from django.contrib import admin

from profiles.models import Follow, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'created_at')
    search_fields = ('user__username', 'bio')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'followed', 'created_at')
    search_fields = ('follower__user__username', 'followed__user__username')
    