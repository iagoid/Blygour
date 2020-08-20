from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


from .models import User, PasswordReset
from .forms import RegisterForm, SettingsAccountForm, PasswordResetForm


def register(request):
    template_name = 'registration/register.html'

    if request.method == 'POST':
        form = RegisterForm(request.POST) or None

        if form.is_valid():
            user = form.save()
            # Atribui ao user o username e senha(antes da criptografia)
            user = authenticate(username=user.username,
                                password=form.cleaned_data['password1'])
            # Faz o login automatico
            login(request, user)
            return redirect('posts:posts-list')

    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, template_name, context)


def password_reset(request):
    template_name = 'users/password_reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Um email foi enviado para você')
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)


def password_reset_confirm(request, key):
    template_name = 'users/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Sua senha foi trocada com sucesso')
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)


@login_required
def edit_account(request):
    template_name = 'users/edit_account.html'
    context = {}

    if request.method == 'POST':
        # Atribui ao post os dados do usuário logado
        form = SettingsAccountForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            form = SettingsAccountForm(instance=request.user)
            messages.success(request, 'Conta Editada com Sucesso')

    else:
        form = SettingsAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def edit_password(request):
    template_name = 'users/edit_password.html'
    context = {}

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Senha Editada com Sucesso')

    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)
