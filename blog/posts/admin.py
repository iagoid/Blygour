from django.contrib import admin
from . models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'image', 'created_at']
    search_fields = ['text', 'title']

admin.site.register(Post, PostAdmin)