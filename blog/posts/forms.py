from django import forms
from django.forms.widgets import ClearableFileInput

from .models import Post, Comments, CommentsAnswer

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'

        # Faz a formatação dos widgets
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': 100,
                'placeholder': 'Título',
                'id': 'postagem_title',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite aqui o seu artigo',
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

class CommentsForm(forms.ModelForm):

    widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite aqui o seu comentário',
            }),
        }

    class Meta:
        model = Comments
        fields = ('comment',)

class CommentsAnswerForm(forms.ModelForm):

    widgets = {
            'answer': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite aqui sua resposta',
            }),
        }

    class Meta:
        model = CommentsAnswer
        fields = ('answer',)