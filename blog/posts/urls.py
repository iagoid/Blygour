from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    
    path('', views.postsList, name='posts-list'),
    path('add-post', views.addPost, name='add-post'),
    path('posts/<int:id>', views.viewPost, name='posts-view'),
    path('delete/<int:id>', views.deletePost, name='delete-post'),
]