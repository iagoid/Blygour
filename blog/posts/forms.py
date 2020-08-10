from django import forms
from django.forms.widgets import ClearableFileInput
from taggit.forms import TagWidget


from .models import Post, Comments

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
                'id': 'textarea-post'
            }),
            'image': forms.ClearableFileInput(attrs={
                'id': 'input-file',
            }),
            'tags': TagWidget(attrs={
                'class': 'form-control',
                'maxlength': 50,
                'placeholder': 'Tags (Separadas por vírgula)',
                'id': 'input-tags'
            }),
        }

        image = forms.ImageField(widget = ClearableFileInput)

        #Mensagens de erro
        error_messages = {
            'text': {
                'required': 'Este campo é obrigatório'
            }
        }

    def clean_tags(self):
        list_tags = self.cleaned_data.get('tags', None)
        if list_tags:
            list_tags = [tags.lower() for tags in list_tags]

        return list_tags

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

