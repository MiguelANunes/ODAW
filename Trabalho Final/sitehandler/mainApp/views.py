from django.shortcuts import render
from django.template import loader
from django.conf import settings
from django.http import HttpResponse
from utils import db_find, db_insert
import hashlib
import dados.Dados

# Create your views here.


def index(request):
    """
    Informa ao usuário que ele está acessando algo que não deveria
    """
    return HttpResponse("Nada para ver aqui")

def login(request):
    """
    Apresenta uma tela de login (que não faz nada)
    """

    userName = request.POST.get("usuario")
    password = request.POST.get("senha")
    filepath = 'mainApp/login.html'

    if userName == None:
        return render(request, filepath)
    
    if userName.isdecimal() or userName.replace(".","",1).isdigit() or userName == None:
        return render(request, filepath, {"message": "Nome de usuário deve ser uma string"})
    elif password == None:
        return render(request, filepath, {"message": "Deve ser inserida uma senha"})

    password = hashlib.sha256(password.encode("utf-8")).hexdigest()
    print("hi")
    if db_find("usuarios", {"userName":userName, "password":password}) != []:
        # se bate o nome e a senha
        return aviao_list(request)
    else:
        return render(request, filepath, {"message": "Usuário ou senha incorretos!"})


def cadastro(request):
    """
    Apresenta uma tela de cadastro (que não faz nada)
    """
    userName       = request.POST.get("userName")
    password       = request.POST.get("senha")
    repeatPassword = request.POST.get("repeatsenha")
    filepath       = 'mainApp/cadastro.html'

    if userName == None:
        return render(request, filepath)
    
    if userName.isdecimal() or userName.replace(".","",1).isdigit() or userName == None:
        return render(request, filepath, {"message": "Nome de usuário deve ser uma string"})
    elif password == None:
        return render(request, filepath, {"message": "Deve ser inserida uma senha"})
    elif repeatPassword == None:
        return render(request, filepath, {"message": "Deve repetir a senha senha"})

    if password != repeatPassword:
        return render(request, filepath, {"message": "Senhas são diferentes"})

    password = hashlib.sha256(password.encode("utf-8")).hexdigest()

    if db_find("usuarios", {"userName":userName}) != []:
        return render(request, filepath, {"message": f"Usuário {userName} já cadastrado"})

    status, message = db_insert("usuarios", {"userName":userName, "password":password})

    if status:
        # se bate o nome e a senha
        return aviao_list(request)
    else:
        return render(request, filepath, {"message": f"{message}"})

def aviao_list(request):
    """
    Retorna todos os aviões no banco
    """
    aviao = dados.Dados.Aviao()
    filepath = 'mainApp/tabelas/aviao.html'
    return aviao.list_all(request, filepath)

def aviao_add(request):
    """
    Atualiza ou adiciona um avião no banco
    """
    aviao = dados.Dados.Aviao()
    filepath = 'mainApp/tabelas/adicionar/adicionar-aviao.html'
    return aviao.add_or_update(request, filepath)

def aviao_delete(request):
    """
    Deleta um avião no banco, se ele existir
    """
    aviao = dados.Dados.Aviao()
    filepath = 'mainApp/tabelas/deletar/deletar-aviao.html'
    return aviao.delete(request, filepath)

def aviao_find(request):
    """
    Retorna todos os aviões que satisfizeram a query do find
    """
    aviao = dados.Dados.Aviao()
    filepath = 'mainApp/tabelas/find/find-aviao.html'
    return aviao.find(request, filepath)

def modelo_list(request):
    """
    Retorna todos os modelos no banco
    """
    modelo = dados.Dados.Modelo()
    filepath = 'mainApp/tabelas/modelo.html'
    return modelo.list_all(request, filepath)

def modelo_add(request):
    """
    Atualiza ou adiciona um modelo no banco
    """
    aviao = dados.Dados.Modelo()
    filepath = 'mainApp/tabelas/adicionar/adicionar-modelo.html'
    return aviao.add_or_update(request, filepath)

def modelo_delete(request):
    """
    Deleta um modelo no banco, se ele existir
    """
    aviao = dados.Dados.Modelo()
    filepath = 'mainApp/tabelas/deletar/deletar-modelo.html'
    return aviao.delete(request, filepath)

def modelo_find(request):
    """
    Retorna todos os modelos que satisfizeram a query do find
    """
    aviao = dados.Dados.Modelo()
    filepath = 'mainApp/tabelas/find/find-modelo.html'
    return aviao.find(request, filepath)

def teste_list(request):
    """
    Retorna todos os testes no banco
    """
    teste = dados.Dados.Teste()
    filepath = 'mainApp/tabelas/teste.html'
    return teste.list_all(request, filepath)

def teste_add(request):
    """
    Insere ou atualiza um teste no banco
    """
    teste = dados.Dados.Teste()
    filepath = 'mainApp/tabelas/adicionar/adicionar-teste.html'
    return teste.add_or_update(request, filepath)

def teste_delete(request):
    """
    Deleta um teste no banco
    """
    teste = dados.Dados.Teste()
    filepath = 'mainApp/tabelas/deletar/deletar-teste.html'
    return teste.delete(request, filepath)

def teste_find(request):
    """
    Retorna todos os testes que satisfizeram a query do find
    """
    teste = dados.Dados.Teste()
    filepath = 'mainApp/tabelas/find/find-teste.html'
    return teste.find(request, filepath)

def sindicato_list(request):
    """
    Retorna todo os sindicatos no banco
    """
    filepath = 'mainApp/tabelas/sindicato.html'
    sindicato = dados.Dados.Sindicato()
    return sindicato.list_all(request, filepath)

def sindicato_add(request):
    """
    Insere ou atualiza um sindicato no banco
    """
    sindicato = dados.Dados.Sindicato()
    filepath = 'mainApp/tabelas/adicionar/adicionar-sindicato.html'
    return sindicato.add_or_update(request, filepath)

def sindicato_delete(request):
    """
    Deleta um sindicato no banco
    """
    sindicato = dados.Dados.Sindicato()
    filepath = 'mainApp/tabelas/deletar/deletar-sindicato.html'
    return sindicato.delete(request, filepath)

def sindicato_find(request):
    """
    Retorna todos os sindicatos que satisfizeram a query do find
    """
    sindicato = dados.Dados.Sindicato()
    filepath = 'mainApp/tabelas/find/find-sindicato.html'
    return sindicato.find(request, filepath)

def controlador_list(request):
    """
    Retorna todos os controladores no banco
    """
    filepath = 'mainApp/tabelas/controlador.html'
    controlador = dados.Dados.Controlador()
    return controlador.list_all(request, filepath)

def controlador_add(request):
    """
    Adiciona ou atualiza um controlador
    """
    filepath = 'mainApp/tabelas/adicionar/adicionar-controlador.html'
    controlador = dados.Dados.Controlador()
    return controlador.add_or_update(request, filepath)

def controlador_delete(request):
    """
    Deleta um controlador do banco
    """
    filepath = 'mainApp/tabelas/deletar/deletar-controlador.html'
    controlador = dados.Dados.Controlador()
    return controlador.delete(request, filepath)

def controlador_find(request):
    """
    Retorna todos os controladores que satisfizeram a query do find
    """
    filepath = 'mainApp/tabelas/find/find-controlador.html'
    controlador = dados.Dados.Controlador()
    return controlador.find(request, filepath)

def tecnico_list(request):
    """
    Retorna todos os técnicos no banco
    """
    filepath = 'mainApp/tabelas/tecnico.html'
    tecnico = dados.Dados.Tecnico()
    return tecnico.list_all(request, filepath)


def tecnico_add(request):
    """
    Adiciona ou atualiza um controlador
    """
    filepath = 'mainApp/tabelas/adicionar/adicionar-tecnico.html'
    tecnico = dados.Dados.Tecnico()
    return tecnico.add_or_update(request, filepath)

def tecnico_delete(request):
    """
    Deleta um tecnico do banco
    """
    filepath = 'mainApp/tabelas/deletar/deletar-tecnico.html'
    tecnico = dados.Dados.Tecnico()
    return tecnico.delete(request, filepath)

def tecnico_find(request):
    """
    Retorna todos os tecnicos que satisfizeram a query do find
    """
    filepath = 'mainApp/tabelas/find/find-tecnico.html'
    tecnico = dados.Dados.Tecnico()
    return tecnico.find(request, filepath)
