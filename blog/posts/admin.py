from django.contrib import admin
from . models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['text', 'image', 'created_at']
    search_fields = ['text']

admin.site.register(Post, PostAdmin)