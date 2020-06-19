from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from . models import Post
from django.contrib import messages
from django.core.paginator import Paginator

def postsList(request):
    posts_list = Post.objects.all().order_by('-created_at')

    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')

    posts = paginator.get_page(page)
    

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('/')

    else:
        form = PostForm()
        return render(request, 'posts/index.html', {'posts': posts, 'form': form})
   
    return render(request, 'posts/index.html', {'posts': posts, 'text':text})

def viewPost(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/postagem.html', {'post': post})

def deletePost(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()

    messages.info(request, 'Postagem Deletada')
    return redirect('/')
