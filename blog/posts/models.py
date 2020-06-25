from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils.crypto import get_random_string
import os

def get_file_path(instance, filename):
    #Pega a extensão do arquivo, pelo ultimo ponto (.png, jpg)
    ext = filename.split(".")[-1]
    #Separa o nome da imagem e randomiza suas letras
    filename = filename + '-' + get_random_string(length=32) + '.' + ext
    return os.path.join(filename)

class Post(models.Model):

    title = models.CharField('Título', max_length=100)
    text = models.TextField('Texto da Postagem')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    #Salva a imagem com um nome randomizado
    image = models.FileField(upload_to = get_file_path, verbose_name='Imagem', null=True, blank=True)

    created_at = models.DateTimeField('Criado em :', auto_now_add = True)
    updated_at = models.DateTimeField('Modificado em :', auto_now = True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
        ordering = ['text']
