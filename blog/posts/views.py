from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from taggit.models import Tag


from users.models import User
from .forms import PostForm, CommentsForm
from .models import Post, Comments

def postsList(request, tag=None):
    search = request.GET.get('search')
    
    tags = Post.tags.all()

    model = Post

    if search:

        posts = Post.objects.order_by('-created_at').filter(title__icontains=search)

        users = User.objects.filter(username__icontains=search)
        template_name = 'posts/search.html'

        context = {
            'posts': posts,
            'users': users,
            'search': search,
            'tags': tags,
        }
        return render(request,template_name, context)

    else:
        # Se foi passado o parametro tag
        if tag:
            posts_list = Post.objects.all().filter(tags__slug__icontains=tag).order_by('-created_at')

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
    template_name = 'posts/details.html'
    post = get_object_or_404(Post, pk=id)
    comments = Comments.objects.all().order_by('-created_at').filter(post = post, parent = None)
    parent_obj = None
    is_liked = False
    
    if request.method == 'POST':
        form = CommentsForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.user = request.user
            comment.post = post
            try:
                parent_id = int(request.POST.get("parent_id"))
            except:
                parent_id = None
            
            if parent_id:
                parent_qs = Comments.objects.filter(id = parent_id)
                if parent_qs.exists() and parent_qs.count() == 1:
                    parent_obj = parent_qs.first()
                    comment.parent = parent_obj
                    

            comment.save()
            messages.success(request, 'Comentário enviado com Sucesso')
            return redirect('posts:posts-view', id=post.id)

    else:
        form = CommentsForm(request.POST)
        is_liked = False

        if comments.filter(likes=request.user):
            is_liked = True
        
        context = {
            'post': post,
            'comments': comments,
            'form': form,
            'parent': parent_obj,
            'is_liked': is_liked,
        }
        return render(request, template_name, context)

def LikeView(request, post, comment):
    comment = get_object_or_404(Comments, id=request.POST.get('comment_id'))
    liked = False
    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
        liked = True
        
    return HttpResponseRedirect(reverse('posts:posts-view', args=[int(post)]))


# Edit das tarefas
@login_required 
def editPost(request, id):
    post = get_object_or_404(Post, pk=id)
    template_name = 'posts/edit_post.html'
    context = {}

    tags = post.tags.all()
    form = PostForm(instance=post)

    if post.user != request.user:
        messages.warning(request, 'Você não tem permissão para fazer isso')
        return redirect('/') 

    context['post'] = post
    context['form'] = form

    if request.method == 'POST' or None:
        form = PostForm(request.POST, request.FILES, instance=post)
        context['form'] = form

        # Faz a verificação do formulário
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form.save_m2m()
            messages.success(request, 'Postagem Editada com Sucesso')
            return redirect('/')
        
        else:
            messages.warning(request, 'Erro ao editar')
            return render(request, template_name, context)

    else:
        return render(request,'posts/edit_post.html', context)

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