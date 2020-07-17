from django.contrib import admin
from .models import Post, Comments

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['text', 'title']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'comment', 'created_at']
    list_filter = ['post', 'created_at', 'user']
    search_fields = ['user', 'post', 'comment']

admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentsAdmin)