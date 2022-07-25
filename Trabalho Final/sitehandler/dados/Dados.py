# Aqui vão ficar as classes e seus respectivos métodos

from utils import db_find, db_insert, db_update, db_delete
from django.shortcuts import render
import datetime

"""
attr = dict() if attr == None else attr
    attr é castado para dict vazio caso não seja passado,
        não é modificado caso seja passado
"""

###########################

def date_parser(date:str):
    """
    Verifica se uma dada string é uma data
    Datas são interpretadas no padrão YYYY-MM-DD
    Retorna a data, caso seja, None caso não seja
    """
    if len(date.split("-")) != 3:
        # se a data não tiver exatamente 3 campos, rejeita
        return None
    if int(date.split("-")[0]) > 2022:
        # se o ano for maior que 2022 rejeita
        return None
    return datetime.datetime.strptime(date, "%Y-%m-%d")

def number_parser(number:str):
    """
    Verifica se uma dada string é um numero
    Retorna o número caso seja, None caso não seja
    """
    if number.isdecimal():
        # se valor procurado é um int
        return int(number)
    elif number.replace(".","",1).isdigit():
        # se o valor procurado é um float
        return float(number)
    else:
        return None

def deletion_handler(request, filePath:str, attrDict:dict, collectionName:str, failMessage:str):
    """
    Função genérica para lidar com a deleção de entradas do banco
    Recebe a requição HTTP, o caminho para o arquivo .html, um dict que associa o nome do
        atributo identificador ao valordo atributo, o nome da coleção e uma mensagem de erro
    Executa uma deleção no banco e retorna a página HTML correspondente
    """
    if db_find(collectionName, attrDict) != []:
        # se a entrada estiver no banco, deleta
        _, message = db_delete(collectionName, attrDict)
        return render(request, filePath, {"message": message})

    else:
        # se não, retorna erro
        return render(request, filePath, {"message": failMessage})

def find_handler(request, filePath:str, collectionName:str, queryString:str):
    """
    Função genérica para lidar com buscas no banco
    Recebe a requição HTTP, o caminho para o arquivo .html, o nome da coleção e a string de busca
    Executa a busca no banco e retorna a página HTML correspondente
    """
    substrings = queryString.split(",")
    # lista de strings da forma ["a:b","c:d",...]
    substrings = [tuple(x.split(":")) for x in substrings]
    # lista de strings da forma [("a","b"),("c","d"),...]

    query = dict()

    for subs in substrings:

        if len(subs) == 1:
            # caso a substring não tenha sido afetada pelo split(":")
            temp = subs[0]

            if "<" in temp:
                key, value = tuple(temp.split("<"))
                value = number_parser(value)
                if value == None:
                    return render(request, filePath, {"message": f"Valor {value} é inválido"})

                query[key] = {"$lt": value}

            elif ">" in temp:
                key, value = tuple(temp.split(">"))
                value = number_parser(value)
                if value == None:
                    return render(request, filePath, {"message": f"Valor {value} é inválido"})

                query[key] = {"$gt": value}

            elif "<=" in temp:
                key, value = tuple(temp.split("<="))
                value = number_parser(value)
                if value == None:
                    return render(request, filePath, {"message": f"Valor {value} é inválido"})

                query[key] = {"$lte": value}

            elif ">=" in temp:
                key, value = tuple(temp.split(">="))
                value = number_parser(value)
                if value == None:
                    return render(request, filePath, {"message": f"Valor {value} é inválido"})

                query[key] = {"$gte": value}

            elif "!=" in temp:
                key, value = tuple(temp.split("!="))
                value = number_parser(value)
                if value == None:
                    return render(request, filePath, {"message": f"Valor {value} é inválido"})

                query[key] = {"$ne": value}

            else:
                return render(request, filePath, {"message": f"{temp} é uma query inválida"})

        else:
            key, value = subs

            temp = number_parser(value)
            if temp == None:
                if date_parser(value.strip("\"")) != None:
                    # se é uma data, passo ela pra query
                    temp = date_parser(value.strip("\""))
                elif value.startswith("\"") and value.endswith("\""):
                    # se o valor é uma string, tiro as aspas
                    # tenho que verificar isso depois das datas se não interpreta datas como strings
                    temp = value.strip("\"")
                else:
                    # se não satisfez nenhum caso, retorna um erro
                    return render(request, filePath, {"message": f"Valor {value} é inválido"})
        
            query[key] = temp

    avioes = db_find(collectionName, query)
    ret = {collectionName: {item['_id']:item for item in avioes}}

    return render(request, filePath, ret)

def add_update_handler(request, filePath:str, collectionName:str, keyAttrDict:dict, attrDict:dict):
    """
    Função genérica para lidar com inserções ou atualizações no banco
    Recebe a requição HTTP, o caminho para o arquivo .html, um dict que associa o nome do
        atributo identificador ao valor do atributo, o nome da coleção e um dict que associa 
        cada atributo ao seu valor
    Executa uma inserção/atualização no banco e retorna o arquivo .html correspondente
    """
    if db_find(collectionName, keyAttrDict) != []:
        # se o atributo chave estiver no banco, atualiza sua entrada
        _, message = db_update(collectionName, keyAttrDict, attrDict)
        return render(request, filePath, {"message": f"{message}"})

    else:
        # se não, insere uma nova
        _, message = db_insert(collectionName, attrDict)
        return render(request, filePath, {"message": f"{message}"})

###########################

class Aviao:
    def __init__(self, attr:dict=None) -> None:
        attr = dict() if attr == None else attr
        self.coda      = attr.get("coda")
        self.codm      = attr.get("codm")
        self.pontuacao = attr.get("pontuacao")

    def __str__(self) -> str:
        return str(self.coda) + " - " + str(self.codm) + " - " + str(self.pontuacao)

    def list_all(self, request, filepath):
        """
        Retorna todos os aviões no banco
        """
        avioes = db_find("avioes", {})
        ret = {'avioes': {item['_id']:item for item in avioes}}

        return render(request, filepath,ret)

    def add_or_update(self, request, filepath):
        """
        Atualiza ou adiciona um avião no banco
        """
        codA      = request.POST.get("coda")
        codM      = request.POST.get("codm")
        pontuacao = request.POST.get("pontuacao")

        if codA == None:
            # se não informou coda, não faz nada
            return render(request, filepath)
        
        # Validações
        if not codM.isdecimal():
            return render(request, filepath, {"message": "Código do Modelo deve ser um número"})
        if not pontuacao.isdecimal():
            return render(request, filepath, {"message": "Pontuação deve ser um número"})
        if not codA.isdecimal():
            # Se chegou aqui é pq recebou algo não nulo, porém não numério
            return render(request, filepath, {"message": "Código do Avião deve ser um número"})

        else:
            codA      = int(codA)
            codM      = int(codM)
            pontuacao = int(pontuacao)

            if db_find("modelos", {"codm": codM}) == []:
                return render(request, filepath, {"message": f"Modelos de código {codM} não está cadastrado"})
            else:
                modelo = db_find("modelos", {"codm": codM})[0]

                if len(modelo["avioes"])+1 <= modelo["limite"]:
                    modelo["avioes"].append(codA)
                    db_update("modelos", {"codm":codM}, modelo)
                else:
                    nome = modelo["nome"]
                    return render(request, filepath, {"message": f"Inserir esse avião iria exceder o limite de aviões do modelo {nome}"})

            return add_update_handler(request, filepath, 'avioes', {'coda':codA}, {"coda":codA, "codm":codM, "pontuacao":pontuacao})

    def delete(self, request, filepath):
        """
        Deleta um avião no banco, se ele existir
        """
        codA = request.POST.get("coda")

        if codA == None:
            # se não informou coda, não faz nada
            return render(request, filepath)

        if not codA.isdecimal():
            # Se chegou aqui é pq recebou algo não nulo, porém não numério
            return render(request, filepath, {"message": "Código do Avião deve ser um número"})

        else:

            aviao = db_find("avioes", {"coda":int(codA)})
            
            if aviao == []:
                return render(request, filepath, {"message": f"Não há avião com coda={codA} no banco"})

            codM = aviao[0]["codm"]

            if db_find("modelos", {"codm": codM}) == []:
                return render(request, filepath, {"message": f"Modelo de código {codM} não está cadastrado"})
            else:
                modelo = db_find("modelos", {"codm": codM})[0]
                modelo["avioes"].remove(int(codA))
                db_update("modelos", {"codm":codM}, modelo)

            return deletion_handler(request,filepath,{"coda":int(codA)},'avioes',f"Não há avião com coda={codA} no banco")

    def find(self, request, filepath):
        """
        Busca por todos os aviões que satisfazem a query passada
        """
        stringBusca = request.POST.get("stringBusca")
        # string da forma "a:b,c:d,..."

        if stringBusca == None:
            return render(request, filepath)

        return find_handler(request, filepath, 'avioes', stringBusca)

###########################

class Controlador:
    def __init__(self, attr:dict=None) -> None:
        attr = dict() if attr == None else attr
        self.matricula  = attr.get("matricula")
        self.nroMembro  = attr.get("nroMembro")
        self.cods       = attr.get("cods")
        self.dataExame  = attr.get("dataExame")
        self.nome       = attr.get("nome")

    def __str__(self) -> str:
        return str(self.matricula) + " - " + str(self.nroMembro) + " - " + str(self.cods) + " - " + str(self.dataExame) + " - " + self.nome

    def list_all(self, request, filepath):
        """
        Retorna todos os controladores no Banco
        """
        controladores = db_find('controladores', {})
        ret = {'controladores': {item['_id']:item for item in controladores}}

        return render(request, filepath, ret)

    def add_or_update(self, request, filepath):
        """
        Atualiza ou adiciona um controlador no banco
        """
        matricula = request.POST.get("matricula")
        nroMembro = request.POST.get("nroMembro")
        dataExame = request.POST.get("data")
        nome      = request.POST.get("nome")
        codS      = request.POST.get("cods")

        if matricula == None:
            # se não informou coda, não faz nada
            return render(request, filepath)

        # Validações        
        if not nroMembro.isdecimal():
            return render(request, filepath, {"message": "Número de Membro deve ser um número"})
        if not codS.isdecimal():
            return render(request, filepath, {"message": "Código do Sindicato deve ser um número"})
        if date_parser(dataExame) == None:
            return render(request, filepath, {"message": f"Data {dataExame} é inválida"})
        if nome.isdecimal() or nome.replace(".","",1).isdigit() or nome == None:
            return render(request, filepath, {"message": "Nome deve ser uma string"})
        if not matricula.isdecimal():
            # Se chegou aqui é pq recebou algo não nulo, porém não numério
            return render(request, filepath, {"message": "Matrícula deve ser um número"})

        else:
            matricula = int(matricula)
            nroMembro = int(nroMembro)
            codS      = int(codS)
            dataExame = date_parser(dataExame)

            if db_find("sindicatos", {"cods": codS}) == []:
                return render(request, filepath, {"message": f"Sindicato de código {codS} não está cadastrado"})
            else:
                sindicato = db_find("sindicatos", {"cods": codS})[0]
                sindicato["controladores"].append(matricula)
                db_update("sindicatos", {"cods":codS}, sindicato)

            return add_update_handler(request, filepath, 'controladores', {'matricula':matricula}, {"matricula":matricula, "cods":codS, 
                "nroMembro":nroMembro, "nome":nome, 'dataExame':dataExame})

    def delete(self, request, filepath):
        """
        Deleta um controlador no banco, se ele existir
        """
        matricula = request.POST.get("matricula")

        if matricula == None:
            # se não informou coda, não faz nada
            return render(request, filepath)

        if not matricula.isdecimal():
            # Se chegou aqui é pq recebou algo não nulo, porém não numério
            return render(request, filepath, {"message": "Matrícula deve ser um número"})

        else:
            controlador = db_find("controladores", {"matricula":int(matricula)})
            
            if controlador == []:
                return render(request, filepath, {"message": f"Não há controladores com matrícula={matricula} no banco"})
            
            codS = controlador[0]["cods"]

            if db_find("sindicatos", {"cods": codS}) == []:
                return render(request, filepath, {"message": f"Sindicato de código {codS} não está cadastrado"})
            else:
                sindicato = db_find("sindicatos", {"cods": codS})[0]
                sindicato["controladores"].remove(int(matricula))
                db_update("sindicatos", {"cods":codS}, sindicato)


            return deletion_handler(request,filepath,{"matricula":int(matricula)},'controladores',f"Não há controladores com matrícula={matricula} no banco")

    def find(self, request, filepath):
        """
        Busca por todos os controladores que satisfazem a query passada
        """
        stringBusca = request.POST.get("stringBusca")
        # string da forma "a:b,c:d,..."

        if stringBusca == None:
            return render(request, filepath)

        return find_handler(request, filepath, 'controladores', stringBusca)

###########################

class Modelo:
    def __init__(self, attr:dict=None) -> None:
        attr = dict() if attr == None else attr
        self.codm       = attr.get("codm")
        self.nome       = attr.get("nome")
        self.capacidade = attr.get("capacidade")
        self.peso       = attr.get("peso")
        self.limite     = attr.get("limite")
        self.avioes     = attr.get("avioes")

    def __str__(self) -> str:
        return str(self.codm) + " - " + self.nome + " - " + str(self.capacidade) + " - " + str(self.peso) + " - " + str(self.limite)

    def list_all(self, request, filepath):
        """
        Retorna todos os modelos no banco
        """
        modelos = db_find('modelos', {})
        ret = {'modelos': {item['_id']:item for item in modelos}}

        return render(request, filepath,ret)

    def add_or_update(self, request, filepath):
        """
        Atualiza ou adiciona um modelo no banco
        """

        codM       = request.POST.get("codm")
        nome       = request.POST.get("nome")
        capacidade = request.POST.get("capacidade")
        peso       = request.POST.get("peso")
        limite     = request.POST.get("limite")

        if codM == None:
            return render(request, filepath)

        # Validações
        if not capacidade.isdecimal():
            return render(request, filepath, {"message": "Capacidade deve ser um número"})
        if not (peso.isdecimal() or peso.replace(".","",1).isdigit()):
            return render(request, filepath, {"message": "Peso deve ser um número"})
        if not limite.isdecimal():
            return render(request, filepath, {"message": "Limite deve ser um número"})
        if nome.isdecimal() or nome.replace(".","",1).isdigit():
            return render(request, filepath, {"message": "Nome deve ser uma string"})
        if not codM.isdecimal():
            return render(request, filepath, {"message": "Código do Modelo deve ser um número"})
        
        else:
            codM       = int(codM)
            capacidade = int(capacidade)
            peso       = int(peso)
            limite     = int(limite)
            
            return add_update_handler(request, filepath, 'modelos', {'codm':codM}, {'codm':codM, "capacidade":capacidade,
                 "peso":peso, "limite":limite, 'nome':nome})

    def delete(self, request, filepath):
        """
        Deleta um modelo do banco
        """

        codM = request.POST.get("codm")
        if codM == None:
            # se não informou coda, não faz nada
            return render(request, filepath)

        if not codM.isdecimal():
            # Se chegou aqui é pq recebou algo não nulo, porém não numério
            return render(request, filepath, {"message": "Código do Modelo deve ser um número"})

        else:
            return deletion_handler(request,filepath,{"codm":int(codM)},'modelos',f"Não há modelo com codm={codM} no banco")

    def find(self, request, filepath):
        """
        Busca por todos os modelos que satisfazem a query passada
        """
        stringBusca = request.POST.get("stringBusca")
        # string da forma "a:b,c:d,..."

        if stringBusca == None:
            return render(request, filepath)

        return find_handler(request, filepath, 'modelos', stringBusca)

###########################

class Teste:
    def __init__(self, attr:dict=None) -> None:
        attr = dict() if attr == None else attr
        self.codt         = attr.get("codt")
        self.coda         = attr.get("coda")
        self.data         = attr.get("data")
        self.duracao      = attr.get("duracao")
        self.pontuacaoMax = attr.get("pontuacaoMax")
    
    def __str__(self) -> str:
        return str(self.codt) + " - " + str(self.coda) + " - " + str(self.data) + " - " + str(self.duracao) + " - " + str(self.pontuacaoMax)

    def list_all(self, request, filepath):
        """
        Retorna todos os testes no banco
        """
        testes = db_find('testes', {})
        ret = {'testes': {item['_id']:item for item in testes}}

        return render(request, filepath,ret)

    def add_or_update(self, request, filepath):
        """
        Atualiza ou adiciona um teste no banco
        """

        codT         = request.POST.get("codt")
        codA         = request.POST.get("coda")
        data         = request.POST.get("data")
        duracao      = request.POST.get("duracao")
        pontuacaoMax = request.POST.get("pontuacaoMax")

        if codT == None:
            return render(request, filepath)

        # Validações
        if not codA.isdecimal():
            return render(request, filepath, {"message": "Código do Avião deve ser um número"})
        if not duracao.isdecimal():
            return render(request, filepath, {"message": "Duração deve ser um número"})
        if not pontuacaoMax.isdecimal():
            return render(request, filepath, {"message": "Pontuação Máxima deve ser um número"})
        if date_parser(data) == None:
            return render(request, filepath, {"message": f"Data {data} é inválida"})
        if not codT.isdecimal():
            return render(request, filepath, {"message": "Código do Teste deve ser um número"})
        
        else:
            codT         = int(codT)
            codA         = int(codA)
            duracao      = int(duracao)
            pontuacaoMax = int(pontuacaoMax)
            data         = date_parser(data)

            return add_update_handler(request, filepath, 'testes', {'codt':codT}, {'codt':codT, "coda":codA,
                 "duracao":duracao, "pontuacaoMax":pontuacaoMax, 'data':data})

    def delete(self, request, filepath):
        """
        Deleta um teste do banco
        """

        codT = request.POST.get("codt")

        if codT == None:
            # se não informou coda, não faz nada
            return render(request, filepath)

        if not codT.isdecimal():
            # Se chegou aqui é pq recebou algo não nulo, porém não numério
            return render(request, filepath, {"message": "Código do Teste deve ser um número"})

        else:
            return deletion_handler(request,filepath,{"codt":int(codT)},'testes',f"Não há teste com codt={codT} no banco")

    def find(self, request, filepath):
        """
        Busca por todos os testes que satisfazem a query passada
        """
        stringBusca = request.POST.get("stringBusca")
        # string da forma "a:b,c:d,..."

        if stringBusca == None:
            return render(request, filepath)

        return find_handler(request, filepath, 'testes', stringBusca)

###########################

class Tecnico:
    def __init__(self, attr:dict=None) -> None:
        attr = dict() if attr == None else attr
        self.matricula = attr.get("matricula")
        self.nroMembro = attr.get("nroMembro")
        self.codm      = attr.get("codm")
        self.cods      = attr.get("cods")
        self.endereco  = attr.get("endereco")
        self.telefone  = attr.get("telefone")
        self.salario   = attr.get("salario")
        self.nome      = attr.get("nome")

    def __str__(self) -> str:
        return str(self.matricula) + " - " + str(self.nroMembro) + " - " + str(self.cods) + " - " + str(self.codModelo) + " - " + self.endereco + " - " + self.telefone + " - " + str(self.salario) + " - " + self.nome

    def list_all(self, request, filepath):
        """
        Retorna todos os técnicos no banco
        """
        tecnicos = db_find('tecnicos', {})
        ret = {'tecnicos': {item['_id']:item for item in tecnicos}}

        return render(request, filepath, ret)

    def add_or_update(self, request, filepath):
        """
        Atualiza ou adiciona um técnico no banco
        """
        matricula = request.POST.get("matricula")
        nroMembro = request.POST.get("nroMembro")
        nome      = request.POST.get("nome")
        codS      = request.POST.get("cods")
        codM      = request.POST.get("codm")
        salario   = request.POST.get("salario")
        telefone  = request.POST.get("telefone")
        endereco  = request.POST.get("endereco")

        if matricula == None:
            # se não informou coda, não faz nada
            return render(request, filepath)
        
        
        # Validações        
        if not nroMembro.isdecimal():
            return render(request, filepath, {"message": "Número de Membro deve ser um número"})
        if not codM.isdecimal():
            return render(request, filepath, {"message": "Código Modelo deve ser um número"})
        if number_parser(salario) == None:
            return render(request, filepath, {"message": "Salário deve ser um número"})
        if not codS.isdecimal():
            return render(request, filepath, {"message": "Código do Sindicato deve ser um número"})
        if nome.isdecimal() or nome.replace(".","",1).isdigit() or nome == None:
            return render(request, filepath, {"message": "Nome deve ser uma string"})
        if telefone.isdecimal() or telefone.replace(".","",1).isdigit() or telefone == None:
            return render(request, filepath, {"message": "Telefone deve ser uma string"})
        if endereco.isdecimal() or endereco.replace(".","",1).isdigit() or endereco == None:
            return render(request, filepath, {"message": "Endereço deve ser uma string"})
        if not matricula.isdecimal():
            # Se chegou aqui é pq recebou algo não nulo, porém não numério
            return render(request, filepath, {"message": "Matrícula deve ser um número"})

        else:
            matricula = int(matricula)
            nroMembro = int(nroMembro)
            codS      = int(codS)
            codM      = int(codM)
            salario   = number_parser(salario)

            if db_find("sindicatos", {"cods": codS}) == []:
                return render(request, filepath, {"message": f"Sindicato de código {codS} não está cadastrado"})
            else:
                sindicato = db_find("sindicatos", {"cods": codS})[0]
                sindicato["tecnicos"].append(matricula)
                db_update("sindicatos", {"cods":codS}, sindicato)

            return add_update_handler(request, filepath, 'tecnicos', {'matricula':matricula}, {"matricula":matricula, "cods":codS, 
                "nroMembro":nroMembro, "nome":nome, 'cods':codS, "codm":codM, 'endereco':endereco, 'telefone':telefone, 'salario':salario})

    def delete(self, request, filepath):
        """
        Deleta um técnico no banco, se ele existir
        """
        matricula = request.POST.get("matricula")

        if matricula == None:
            # se não informou coda, não faz nada
            return render(request, filepath)

        if not matricula.isdecimal():
            # Se chegou aqui é pq recebou algo não nulo, porém não numério
            return render(request, filepath, {"message": "Matrícula deve ser um número"})

        else:

            tecnico = db_find("tecnicos", {"matricula":int(matricula)})
            
            if tecnico == []:
                return render(request, filepath, {"message": f"Não há tecnicos com matrícula={matricula} no banco"})
            
            codS = tecnico[0]["cods"]

            if db_find("sindicatos", {"cods": codS}) == []:
                return render(request, filepath, {"message": f"Sindicato de código {codS} não está cadastrado"})
            else:
                sindicato = db_find("sindicatos", {"cods": codS})[0]
                sindicato["tecnicos"].remove(int(matricula))
                db_update("sindicatos", {"cods":codS}, sindicato)

            return deletion_handler(request,filepath,{"matricula":int(matricula)},'tecnicos',f"Não há técnicos com matrícula={matricula} no banco")

    def find(self, request, filepath):
        """
        Busca por todos os técnicos que satisfazem a query passada
        """
        stringBusca = request.POST.get("stringBusca")
        # string da forma "a:b,c:d,..."

        if stringBusca == None:
            return render(request, filepath)

        return find_handler(request, filepath, 'tecnicos', stringBusca)

###########################

class Sindicato:
    def __init__(self, attr:dict=None) -> None:
        attr = dict() if attr == None else attr
        self.nome          = attr.get("nome")
        self.cods          = attr.get("cods")
        self.controladores = attr.get("controladores")
        self.tecnicos      = attr.get("tecnicos")

    def __str__(self) -> str:
        return self.nome + " - " + str(self.codSindicato) 

    def list_all(self, request, filepath):
        """
        Retorna todos os sindicatos no banco
        """
        sindicatos = db_find('sindicatos', {})
        ret = {'sindicatos': {item['_id']:item for item in sindicatos}}
        
        return render(request, filepath, ret)

    def add_or_update(self, request, filepath):
        """
        Atualiza ou adiciona um sindicato no banco
        """

        nome = request.POST.get("nome")
        codS = request.POST.get("cods")

        if codS == None:
            return render(request, filepath)

        # Validações
        if nome.isdecimal() or nome.replace(".","",1).isdigit() or nome == None:
            return render(request, filepath, {"message": "Nome deve ser uma string"})
        if not codS.isdecimal():
            return render(request, filepath, {"message": "Código do Sindicato deve ser um número"})
        
        else:
            codS = int(codS)

            if db_find("sindicatos", {"cods":codS}) == []:
                tecnicos      = []
                controladores = []
            else:
                sindicato     = db_find("sindicatos", {"cods":codS})[0]
                tecnicos      = sindicato["tecnicos"]
                controladores = sindicato["controladores"]
                pass

            return add_update_handler(request, filepath, 'sindicatos', {'cods':codS}, {'cods':codS, "nome":nome, 
                "tecnicos":tecnicos, "controladores":controladores})

    def delete(self, request, filepath):
        """
        Deleta um teste do banco
        """

        codS = request.POST.get("cods")

        if codS == None:
            # se não informou coda, não faz nada
            return render(request, filepath)

        if not codS.isdecimal():
            # Se chegou aqui é pq recebou algo não nulo, porém não numério
            return render(request, filepath, {"message": "Código do Sindicato deve ser um número"})

        else:
            return deletion_handler(request,filepath,{"cods":int(codS)},'sindicatos',f"Não há sindicato com cods={codS} no banco")

    def find(self, request, filepath):
        """
        Busca por todos os testes que satisfazem a query passada
        """
        stringBusca = request.POST.get("stringBusca")
        # string da forma "a:b,c:d,..."

        if stringBusca == None:
            return render(request, filepath)

        return find_handler(request, filepath, 'sindicatos', stringBusca)
