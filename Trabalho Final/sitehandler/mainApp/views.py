from django.shortcuts import render
from django.template import loader
from django.conf import settings
from django.http import HttpResponse
import dbconnection

from utils import get_db_handle


# Create your views here.

def index(request):
    return HttpResponse("Nada para ver aqui")

def login(request):
    return render(request, 'mainApp/login.html')

def find(request):
    return render(request, 'mainApp/find.html')

def cadastro(request):
    return render(request, 'mainApp/cadastro.html')

def aviao(request):
    _, aeroporto = get_db_handle()
    avioes = dbconnection.find(aeroporto, 'avioes', {})

    ret = {'avioes': {item['_id']:item for item in avioes}}

    return render(request, 'mainApp/tabelas/aviao.html',ret)

def modelo(request):
    _, aeroporto = get_db_handle()
    modelos = dbconnection.find(aeroporto, 'modelos', {})

    ret = {'modelos': {item['_id']:item for item in modelos}}

    return render(request, 'mainApp/tabelas/modelo.html',ret)

def teste(request):
    _, aeroporto = get_db_handle()
    testes = dbconnection.find(aeroporto, 'testes', {})

    ret = {'testes': {item['_id']:item for item in testes}}

    return render(request, 'mainApp/tabelas/teste.html',ret)

def sindicato(request):
    _, aeroporto = get_db_handle()
    sindicatos = dbconnection.find(aeroporto, 'sindicatos', {})

    ret = {'sindicatos': {item['_id']:item for item in sindicatos}}

    return render(request, 'mainApp/tabelas/sindicato.html',ret)

def controlador(request):
    _, aeroporto = get_db_handle()
    controladores = dbconnection.find(aeroporto, 'controladores', {})

    ret = {'controladores': {item['_id']:item for item in controladores}}

    return render(request, 'mainApp/tabelas/controlador.html',ret)

def tecnico(request):
    _, aeroporto = get_db_handle()
    tecnicos = dbconnection.find(aeroporto, 'tecnicos', {})

    ret = {'tecnicos': {item['_id']:item for item in tecnicos}}

    return render(request, 'mainApp/tabelas/tecnico.html',ret)