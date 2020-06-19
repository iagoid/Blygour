from django.db import models

from django.utils.crypto import get_random_string
import os

def get_file_path(instance, filename):
    #Pega a extensão do arquivo, pelo ultimo ponto (.png, jpg)
    ext = filename.split(".")[-1]
    #Separa o nome da imagem e randomiza suas letras
    filename = filename + '-' + get_random_string(length=32) + '.' + ext
    return os.path.join(filename)

class Post(models.Model):

    text = models.TextField()
    #Salva a imagem com um nome randomizado
    image = models.FileField(upload_to = get_file_path)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.text