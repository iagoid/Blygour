from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    
    path('', views.postsList, name='posts-list'),
    path('tag/<str:tag>/', views.postsList, name='index_tagged'),

    path('add-post', views.addPost, name='add-post'),
    path('<int:id>', views.viewPost, name='posts-view'),
    path('delete/<int:id>', views.deletePost, name='delete-post'),
    path('edit/<int:id>', views.editPost, name='edit-post'),
    path('profile/<str:username>/', views.profileUser, name='profile_user'),
]