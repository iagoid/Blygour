from django.urls import path
from . import views

#Aqui são definidas quais URL o app user pode acessar e qual função ele chama
urlpatterns = [
    path('register/', views.SignUp.as_view(), name="SignUp")
]

#localhost:8000 / URL do Arquivo Principal / essa URL
