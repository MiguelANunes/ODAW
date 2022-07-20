from django.urls import path
from mainApp import views

app_name = "Aeroporto"

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadstro'),
    path('find/', views.find, name='find')
]