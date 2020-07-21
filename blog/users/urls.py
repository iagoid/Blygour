from django.urls import path
from . import views
from django.conf import settings

#Aqui são definidas quais URL o app user pode acessar e qual função ele chama
app_name = 'users'
urlpatterns = [
    path('register/', views.register, name="signup"),
    path('new_password/', views.password_reset, name='password_reset'),
    path('confirm_new_password/<str:key>', views.password_reset_confirm, name='password_reset_confirm'),
    path('settings/', views.edit_account, name="edit_account"),
    path('settings/password/', views.edit_password, name='edit_password'),
]


#localhost:8000 / URL do Arquivo Principal / essa URL
