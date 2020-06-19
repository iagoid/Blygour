from django import forms
from django.forms.widgets import ClearableFileInput

from .models import Post

class PostForm(forms.ModelForm):
    
    
    class Meta:
        model = Post
        fields = '__all__'

        # Faz a formatação dos widgets
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'maxlenght': 255,
                'placeholder': 'O que está acontecendo?',
            }),
            'image': forms.ClearableFileInput(attrs={
                'id': 'input-file',

            }),
        }

        image = forms.ImageField(widget = ClearableFileInput)

        #Mensagens de erro
        error_messages = {
            'text': {
                'required': 'Este campo é obrigatório'
            }
        }