from django.urls import path
from mainApp import views

app_name = "Aeroporto"

urlpatterns = [
    path('',             views.login, name='index'),
    path('login/',       views.login, name='login'),
    path('cadastro/',    views.cadastro, name='cadastro'),
    path('aviao/',       views.aviao, name='aviao'),
    path('modelo/',      views.modelo, name='modelo'),
    path('teste/',       views.teste, name='teste'),
    path('sindicato/',   views.sindicato, name='sindicato'),
    path('controlador/', views.controlador, name='controlador'),
    path('tecnico/',     views.tecnico, name='tecnico'),
    path('find/',        views.find, name='find')
]