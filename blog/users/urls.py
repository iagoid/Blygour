from django.urls import path
from . import views
from django.conf import settings

#Aqui são definidas quais URL o app user pode acessar e qual função ele chama
app_name = 'users'
urlpatterns = [
    path('register/', views.register, name="signup"),
    path('settings/', views.settings, name="settings"),
    path('settings/password/', views.edit_password, name='edit_password'),
    
]

#localhost:8000 / URL do Arquivo Principal / essa URL
