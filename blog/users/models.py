from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.utils.crypto import get_random_string
from django.utils.html import mark_safe
import os


def get_file_path(instance, filename):
    # Pega a extenção do arquivp
    ext = filename.split('.')[-1]
    # Separa o nome da imagem e randomiza as letras
    filename = filename + '-' + get_random_string(length=32) + '.' + ext
    return os.path.join('profiles', filename)

class User(AbstractUser, PermissionsMixin):
    username = models.CharField('Nome do usuário', max_length=30, unique=True)
    email = models.EmailField('Email', unique=True)
    profile_picture = models.ImageField(upload_to = get_file_path, verbose_name='Imagem', null=True, blank=True)
    # Campos Compativeis
    is_active = models.BooleanField('Está Ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    is_superuser = models.BooleanField('É super Usuário?', blank=True, default=False)
    date_joined = models.DateField('Data de Entrada', auto_now_add=True)

    first_name = None
    last_name = None

    objects = UserManager()

    # Usado no campo login
    USERNAME_FIELD = 'username'
    # Usado no Cadastro do usuário
    REQUIRED_FIELDS = ['email']

    @property
    def admin_photo(self):
        return mark_safe('<img src="{}" width="200px" />'.format(self.profile_picture.url))
        self.admin_photo.short_description = "Imagem Postagem"
        self.admin_photo.allow_tags = True

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    def __str__(self):
        return self.username
        
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'