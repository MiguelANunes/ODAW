from django.urls import path
from mainApp import views

app_name = "Aeroporto"

urlpatterns = [
    path('',             views.login,                 name='index'),

    path('login/',       views.login,                 name='login'),
    path('cadastro/',    views.cadastro,              name='cadastro'),

    path('aviao/',       views.aviao_list,            name='aviao'),
    path('aviao/add/',   views.aviao_add,             name='aviao_add'),
    path('aviao/delete/',views.aviao_delete,          name='aviao_delete'),
    path('aviao/find/',  views.aviao_find,            name='aviao_find'),

    path('modelo/',      views.modelo_list,           name='modelo'),
    path('modelo/add/',   views.modelo_add,           name='modelo_add'),
    path('modelo/delete/',views.modelo_delete,        name='modelo_delete'),
    path('modelo/find/',  views.modelo_find,          name='modelo_find'),

    path('teste/',        views.teste_list,           name='teste'),
    path('teste/add/',    views.teste_add,            name='teste_add'),
    path('teste/delete/', views.teste_delete,         name='teste_delete'),
    path('teste/find/',   views.teste_find,           name='teste_find'),

    path('sindicato/',        views.sindicato_list,   name='sindicato'),
    path('sindicato/add/',    views.sindicato_add,    name='sindicato_add'),
    path('sindicato/delete/', views.sindicato_delete, name='sindicato_delete'),
    path('sindicato/find/',   views.sindicato_find,   name='sindicato_find'),

    path('controlador/',        views.controlador_list,   name='controlador'),
    path('controlador/add/',    views.controlador_add,    name='controlador_add'),
    path('controlador/delete/', views.controlador_delete, name='controlador_delete'),
    path('controlador/find/',   views.controlador_find,   name='controlador_find'),

    path('tecnico/',        views.tecnico_list,           name='tecnico'),
    path('tecnico/add/',    views.tecnico_add,            name='tecnico_add'),
    path('tecnico/delete/', views.tecnico_delete,         name='tecnico_delete'),
    path('tecnico/find/',   views.tecnico_find,           name='tecnico_find')
]