from django.urls import path
from . import views

#Aqui são definidas quais URL o app user pode acessar e qual função ele chama
app_name = 'users'
urlpatterns = [
    path('register/', views.SignUp.as_view(), name="signup")
]

#localhost:8000 / URL do Arquivo Principal / essa URL
