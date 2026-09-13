from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from posts.models import Post
from profiles.models import Follow, UserProfile


def profile_detail(request, username):
    """Muestra el perfil de un usuario con sus publicaciones."""
    user = get_object_or_404(User, username=username)
    profile = getattr(user, 'profile', None)
    if profile is None:
        profile = UserProfile.objects.create(user=user)

    posts = Post.objects.filter(author=user).select_related('author').prefetch_related('comments__author', 'likes').order_by('-created_at')
    followers_count = Follow.objects.filter(followed=profile).count()
    following_count = Follow.objects.filter(follower=profile).count()

    is_owner = request.user.is_authenticated and request.user == user
    is_following = False

    if request.user.is_authenticated and request.user != user:
        current_profile = UserProfile.objects.get_or_create(user=request.user)[0]
        is_following = Follow.objects.filter(follower=current_profile, followed=profile).exists()

    return render(request, 'profiles/profile_detail.html', {
        'user': user,
        'profile': profile,
        'posts': posts,
        'followers_count': followers_count,
        'following_count': following_count,
        'is_owner': is_owner,
        'is_following': is_following,
    })


@login_required
def edit_profile(request):
    """Permite editar el perfil del usuario logueado."""
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        bio = request.POST.get('bio', '').strip()
        birth_date = request.POST.get('birth_date')
        profile_picture = request.FILES.get('profile_picture')

        if bio:
            profile.bio = bio
        if birth_date:
            profile.birth_date = birth_date
        if profile_picture:
            profile.profile_picture = profile_picture

        profile.save()
        messages.success(request, 'Tu perfil se ha actualizado correctamente.')
        return redirect('profile_detail', username=request.user.username)

    return render(request, 'profiles/edit_profile.html', {'profile': profile})


@login_required
def toggle_follow(request, username):
    """Sigue o deja de seguir a otro usuario."""
    target_user = get_object_or_404(User, username=username)
    if request.user == target_user:
        return redirect('profile_detail', username=username)

    target_profile = UserProfile.objects.get_or_create(user=target_user)[0]
    current_profile = UserProfile.objects.get_or_create(user=request.user)[0]

    relation = Follow.objects.filter(follower=current_profile, followed=target_profile).first()
    if relation:
        relation.delete()
        messages.info(request, f'Has dejado de seguir a {target_user.username}.')
    else:
        Follow.objects.create(follower=current_profile, followed=target_profile)
        messages.success(request, f'Ahora estás siguiendo a {target_user.username}.')

    return redirect('profile_detail', username=username)


def register_view(request):
    """Vista para registrar un nuevo usuario."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.get_or_create(user=user)
            login(request, user)
            messages.success(request, 'Registro correcto. ¡Bienvenido!')
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
