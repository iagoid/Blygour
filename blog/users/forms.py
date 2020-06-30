from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
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

class SettingsAccountForm(forms.ModelForm):

    # Qual model vai ser pego e quais seus campos
    class Meta:
        model = User
        fields = ['username', 'email','profile_picture']
