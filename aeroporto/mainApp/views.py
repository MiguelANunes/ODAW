from django.shortcuts import render
import django.http
from utils import get_db_handle
import pymongo
from django.conf import settings

# Create your views here.

def index(request):
    db, client = get_db_handle()

    avioes_collection = db['avioes']
    avioes = avioes_collection.find()

    ret = {}

    for aviao in avioes:
        ret.append(aviao)
    
    return django.http.HttpResponse(ret)


