from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from users.models import User
from .forms import PostForm
from .models import Post

def postsList(request):
    posts_list = Post.objects.all().order_by('-created_at')

    paginator = Paginator(posts_list, 7)
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
    context = {
        'post': post
    }
    return render(request, 'posts/details.html', context)

# Edit das tarefas
@login_required 
def editPost(request, id):
    post = get_object_or_404(Post, pk=id)
    #Deixa o formulário preenchido com os dado criados
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        # Faz a verificação do formulário
        if form.is_valid():
            post.user = request.user
            post.save()
            messages.success(request, 'Postagem Editada com Sucesso')
            return redirect('/') 
        
        else:
            return render(request,'posts/edit_post.html', {'form': form, 'post': post})

    else:
        return render(request,'posts/edit_post.html', {'form': form, 'post': post})


@login_required
def deletePost(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()

    messages.success(request, 'Postagem Deletada')
    return redirect('/')

def profile_user(request, username):
    user = get_object_or_404(User, username = username)
    template_name = 'posts/user_details.html'

    posts_list = Post.objects.all().order_by('-created_at').filter(user = user)

    paginator = Paginator(posts_list, 7)
    page = request.GET.get('page')

    posts = paginator.get_page(page)
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, template_name, context)