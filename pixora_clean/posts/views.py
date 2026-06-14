from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from .models import Post, Like, Comment, Follow

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password1)
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'registration/register.html', {'error': 'Username already taken!'})
        else:
            return render(request, 'registration/register.html', {'error': 'Passwords do not match!'})
    return render(request, 'registration/register.html')

@login_required
def home(request):
    following_users = Follow.objects.filter(follower=request.user).values_list('following', flat=True)
    posts = Post.objects.filter(user__in=following_users).order_by('-created_at')
    return render(request, 'posts/home.html', {'posts': posts})

@login_required
def explore(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/explore.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        caption = request.POST.get('caption', '')
        if image:
            Post.objects.create(user=request.user, image=image, caption=caption)
            return redirect('home')
    return render(request, 'posts/create_post.html')

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    post.delete()
    return redirect('home')

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')
    liked = Like.objects.filter(user=request.user, post=post).exists()
    return render(request, 'posts/post_detail.html', {
        'post': post,
        'comments': comments,
        'liked': liked,
        'like_count': post.likes.count()
    })

@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
    return JsonResponse({'liked': liked, 'count': post.likes.count()})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        if text:
            Comment.objects.create(user=request.user, post=post, text=text)
    return redirect('post_detail', post_id=post_id)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    post_id = comment.post.id
    comment.delete()
    return redirect('post_detail', post_id=post_id)

@login_required
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=profile_user).order_by('-created_at')
    is_following = Follow.objects.filter(follower=request.user, following=profile_user).exists()
    followers_count = Follow.objects.filter(following=profile_user).count()
    following_count = Follow.objects.filter(follower=profile_user).count()
    return render(request, 'posts/profile.html', {
        'profile_user': profile_user,
        'posts': posts,
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count,
    })

@login_required
def toggle_follow(request, username):
    target_user = get_object_or_404(User, username=username)
    if request.user == target_user:
        return redirect('profile', username=username)
    follow, created = Follow.objects.get_or_create(follower=request.user, following=target_user)
    if not created:
        follow.delete()
    return redirect('profile', username=username)
