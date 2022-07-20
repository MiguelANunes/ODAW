from django.shortcuts import render
from django.template import loader
from django.conf import settings
from django.http import HttpResponse
import dbconnection

from utils import get_db_handle


# Create your views here.

def index(request):
    client, aeroporto = get_db_handle()

    avioes_collection = aeroporto['avioes']
    avioes = avioes_collection.find()

    ret = []

    for aviao in avioes:
        ret.append(f"coda:{aviao['coda']}; codm:{aviao['codm']}; pontuacao{aviao['pontuacao']}<br>")
    
    return HttpResponse(ret)

def login(request):
    return render(request, 'mainApp/login.html')

def find(request):
    client, aeroporto = get_db_handle()
    # avioes = aeroporto['avioes']

    avioes = dbconnection.find(aeroporto, 'avioes', {})

    ret = {item['_id']:item for item in avioes}

    return render(request, 'mainApp/find.html', ret)

def cadastro(request):
    return render(request, 'mainApp/cadastro.html', {'teste':"Olá, isso é um teste"})