from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm


from .forms import RegisterForm, SettingsAccountForm

def register(request):
    template_name = 'registration/register.html'

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            # Atribui ao user o username e senha(antes da criptografia)
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            # Faz o login automatico
            login(request, user)
            return redirect('posts:posts-list')

    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, template_name, context)

@login_required
def settings(request):
    template_name = 'registration/settings.html'
    context = {}

    if request.method == 'POST':
        # Atribui ao post os dados do usuário logado
        form = SettingsAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = SettingsAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = SettingsAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)

@login_required
def edit_password(request):
    template_name = 'registration/edit_password.html'
    context = {}

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)
