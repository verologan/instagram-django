from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Comment, Like, Post


def home_feed(request):
    """Vista principal del feed con publicaciones recientes."""
    posts = Post.objects.select_related('author').prefetch_related('comments__author', 'likes').all()[:10]
    for post in posts:
        post.user_has_liked = post.likes.filter(user=request.user).exists() if request.user.is_authenticated else False
    return render(request, 'posts/post_feed.html', {'posts': posts})


def post_detail(request, post_id):
    """Muestra el detalle completo de una publicación y permite comentar."""
    post = get_object_or_404(Post.objects.select_related('author').prefetch_related('comments__author', 'likes'), id=post_id)
    post.user_has_liked = post.likes.filter(user=request.user).exists() if request.user.is_authenticated else False

    return render(request, 'posts/post_detail.html', {'post': post})


@login_required
def create_post(request):
    """Permite crear una publicación si el usuario está autenticado."""
    if request.method == 'POST':
        caption = request.POST.get('caption', '').strip()
        image = request.FILES.get('image')

        if caption or image:
            Post.objects.create(
                author=request.user,
                caption=caption,
                image=image,
            )
            messages.success(request, 'Tu publicación se ha creado correctamente.')
            return redirect('post_feed')

    return render(request, 'posts/create_post.html')


@login_required
def toggle_like(request, post_id):
    """Añade o quita un like de una publicación."""
    post = get_object_or_404(Post, id=post_id)
    like = post.likes.filter(user=request.user).first()

    if like:
        like.delete()
    else:
        Like.objects.create(post=post, user=request.user)

    return redirect(request.META.get('HTTP_REFERER', 'post_feed'))


@login_required
def add_comment(request, post_id):
    """Añade un comentario a una publicación."""
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        if text:
            Comment.objects.create(post=post, author=request.user, text=text)
            messages.success(request, 'Tu comentario se ha publicado.')
    return redirect('post_detail', post_id=post.id)

