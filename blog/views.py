from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {
        "posts":posts
    })
def detalle(request, title):
    post = Post.objects.get(title=title)
    print(post)
    return render(request, 'blog/detalle.html', {
        "post":post
    })

def new(request):
    post = Post.objects.all()
    return render(request, 'blog/new_post.html', {
        "post":post
    })




