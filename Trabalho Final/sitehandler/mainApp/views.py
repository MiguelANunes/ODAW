from django.shortcuts import render
from django.template import loader
from django.conf import settings
from django.http import HttpResponse

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


def detail(request, num):
    return HttpResponse(f"Isso é um teste {num}")

def login(request):
    return render(request, 'mainApp/login.html')