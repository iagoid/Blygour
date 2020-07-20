from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_superuser', 'date_joined']
    readonly_fields = ('visualizar_imagem', )

    list_filter = ['is_superuser']
    search_fields = ['username', 'email']
    fields = ['username', 'email', 'password', 'profile_picture', 'visualizar_imagem', 'is_staff', 'is_superuser']


    def visualizar_imagem(self, obj):
        return obj.admin_photo
    visualizar_imagem.short_description = "Foto de perfil"


admin.site.register(User, UserAdmin)