from django.contrib import admin
from .models import Post, Comments, CommentsAnswer

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['text', 'title']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'comment', 'created_at']
    list_filter = ['post', 'created_at', 'user']
    search_fields = ['user', 'post', 'comment']

class CommentsAnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'answer', 'comment', 'created_at']
    list_filter = ['answer', 'created_at', 'user']
    search_fields = ['user', 'answer', 'comment']

admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(CommentsAnswer, CommentsAnswerAdmin)
