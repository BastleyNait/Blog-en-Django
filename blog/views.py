from django.shortcuts import redirect, render 
from .models import Post
from django.utils import timezone 
from .forms import PostForm 
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {
        "posts":posts
    })
def detalle(request, pk):
    post = Post.objects.get(pk=pk)
    print(post)
    return render(request, 'blog/detalle.html', {
        "post":post
    })

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detalle', pk=post.pk)

    else:
        form = PostForm()
    return render(request, 'blog/new_post.html', {
        "form":form
    })




