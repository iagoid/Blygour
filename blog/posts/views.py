from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from users.models import User
from .forms import PostForm, CommentsForm
from .models import Post, Comments

def postsList(request):
    search = request.GET.get('search')
    
    tags = Post.tags.all()

    model = Post

    if search:
        posts = Post.objects.filter(title__icontains=search)
        users = User.objects.filter(username__icontains=search)

        context = {
            'posts': posts,
            'users': users,
            'search': search,
            'tags': tags,
        }
        return render(request, 'posts/search.html', context)

    else:
        posts_list = Post.objects.all().order_by('-created_at')

        paginator = Paginator(posts_list, 7)
        page = request.GET.get('page')

        posts = paginator.get_page(page)

        context = {
            'posts': posts,
            'tags': tags,
        }
            
        return render(request, 'posts/index.html', context)
            
@login_required
def addPost(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            form.save_m2m()
            messages.success(request, 'Postagem Publicada com Sucesso')
            return redirect('/')

    else:
        form = PostForm(request.POST, request.FILES)
        return render(request, 'posts/add-post.html', {'form': form})
        

# Detalhes dos posts
def viewPost(request, id):
    post = get_object_or_404(Post, pk=id)
    comments = Comments.objects.all().order_by('-created_at').filter(post = post)
    
    if request.method == 'POST':
        form = CommentsForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Comentário enviado com Sucesso')
            return redirect('posts:posts-view', id=post.id)

    else:
        form = CommentsForm(request.POST)
        
        context = {
            'post': post,
            'comments': comments,
            'form': form,
        }
        return render(request, 'posts/details.html', context)

# Edit das tarefas
@login_required 
def editPost(request, id):
    post = get_object_or_404(Post, pk=id)
    #Deixa o formulário preenchido com os dado criados
    form = PostForm(instance=post)

    if post.user == request.user:

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

    else:
        messages.warning(request, 'Você não tem permissão para fazer isso')
        return redirect('/') 


@login_required
def deletePost(request, id):
    post = get_object_or_404(Post, pk=id)
    if post.user == request.user:
        post.delete()

        messages.success(request, 'Postagem Deletada')
        return redirect('/')

    else:
        messages.warning(request, 'Você não tem permissão para fazer isso')
        return redirect('/') 


def profileUser(request, username):
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