from django.contrib import admin
from .models import Post, Comments

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'created_at']
    readonly_fields = ('visualizar_imagem', )
    list_filter = ['created_at']
    search_fields = ['text', 'title']

    def visualizar_imagem(self, obj):
        return obj.view_image
    visualizar_imagem.short_description = "Imagem Postagem"

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'comment', 'created_at']
    list_filter = ['post', 'created_at', 'user']
    search_fields = ['user', 'post', 'comment']

admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentsAdmin)