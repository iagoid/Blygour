from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.postsList, name='posts-list'),
    path('posts/<int:id>', views.viewPost, name='posts-view'),
    path('delete/<int:id>', views.deletePost, name='delete-post')
]