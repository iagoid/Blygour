from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    field_order = ['username', 'email']

    # Função para não ser possível cadastrar email iguais
    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já foi cadastrado')

        return email

    # Substitui o save padrão do UserCreation
    def save(self, commit=True):
        # Chama o super para validar o user e a password, mas não salva
        user = super(RegisterForm, self).save(commit=False)
        # Retorna o email já transformado em objeto Python
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class SettingsAccountForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        # Exclui da busca o usuário atual
        queryset = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        # Filtra o email e retorna True ou False
        if queryset.exists():
            # Se existir retorna um erro de validação
            raise forms.ValidationError('Este email já foi cadastrado')
    
        return email

    # Qual model vai ser pego e quais seus campos
    class Meta:
        model = User
        fields = ['username', 'email']
