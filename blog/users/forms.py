from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from posts.utils import generate_hash_key
from posts.mail import send_mail_template
from django.core.validators import RegexValidator

from.models import PasswordReset

User = get_user_model()

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Apenas caracteres AlfaNuméricos')

class RegisterForm(UserCreationForm):

    username = forms.CharField(validators=[alphanumeric])
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

    # Verificação das senhas
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Sua confirmação não está correta')
        return password2

    # Substitui o save padrão do UserCreation
    def save(self, commit=True):
        # Chama o super para validar o user e a password, mas não salva
        user = super(RegisterForm, self).save(commit=False)
        # Retorna o email já transformado em objeto Python
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email']

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='Email')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError('Nenhum usuário com este email')

    def save(self):
        user = User.objects.get(email = self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        template_name = 'users/password_reset_mail.html'
        context = {
            'reset': reset,
        }
        subject = 'Criar nova senha no Blygour'
        send_mail_template(subject, template_name, context, [user.email])


class SettingsAccountForm(forms.ModelForm):
    username = forms.CharField(validators=[alphanumeric])


    # Qual model vai ser pego e quais seus campos
    class Meta:
        model = User
        fields = ['username', 'email','profile_picture']

