from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from . models import Post
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def postsList(request):
    posts_list = Post.objects.all().order_by('-created_at')

    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')

    posts = paginator.get_page(page)
    
    return render(request, 'posts/index.html', {'posts': posts})

@login_required
def addPost(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            messages.success(request, 'Postagem Publicada com Sucesso')
            return redirect('/')

    else:
        form = PostForm(request.POST, request.FILES)
        return render(request, 'posts/add-post.html', {'form': form})
        

def viewPost(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/details.html', {'post': post})

@login_required
def deletePost(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()

    messages.success(request, 'Postagem Deletada')
    return redirect('/')
