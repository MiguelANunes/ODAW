# Aqui vai ficar a conectividade com o banco de dados

# pip install pymongo
# https://pymongo.readthedocs.io/en/stable/
# pip install dnspython
# https://www.dnspython.org/

# https://www.mongodb.com/languages/python

import pymongo, pymongo.errors, sys

def init_connection(connectionString:str):
    """
    Função que começa a conexão com o banco de dados
    Retorna o objeto de conexão com o banco caso teve sucesso, retorna False otherwise
    """

    try:        
        client = pymongo.MongoClient(connectionString)
    except pymongo.errors.ConnectionFailure as E:
        print(E)
        print("Erro ao iniciar a conexão", file=sys.stderr)
        return False

    # isso me retorna a database "Aeroporto" na conexão
    # Não posso retornar a DB inteira, tenho que retornar apenas a conexão, chamo a DB um nível acima
    return client#['Aeroporto']

def close_conection(database:pymongo.MongoClient) -> bool:
    """
    Função que termina a conexão com o banco de dados
    Retorna True se conseguiu terminar, False se não conseguiu
    https://stackoverflow.com/questions/18401015/how-to-close-a-mongodb-python-connection
    """
    try:
        database.close()
    except pymongo.errors.InvalidOperation as E: 
        # Não sei se é necessário tentar capturar erros aqui, não lembro de ter visto algo
        # sobre erros ao fechar a conexão na documentação, mas vou deixar por via das duvidas
        print(E)
        print("Erro ao terminar a conexão", file=sys.stderr)
        return False

    return True

def find(aeroporto, nomeColecao:str, filter:dict) -> list:
    """
    Função que busca dados no DB
    Recebe o nome da coleção e opcionalmente um dict de filtro
    Retorna uma lista de todos os dados que foram encontrados
    """
    colecao    = aeroporto[nomeColecao]
    returnList = []

    if filter == {}:
        for objeto in colecao.find():
            returnList.append(objeto)
    else:
        for objeto in colecao.find(filter):
            returnList.append(objeto)

    return returnList
    
def insert(aeroporto, nomeColecao:str, dados:dict) -> tuple:
    """
    Função que insere dados no DB 
    Recebe o nome da coleção onde serão inseridos os dados
    Dados são passados para essa função em forma de dict
    Retorna uma tupla contendo um booleano indicando sucesso/fracasso ao inserir e uma 
        mensagem de resposta
    """
    colecao  = aeroporto[nomeColecao]

    if dados == {}:
        return (False, "Nenhum dado fornecido!")

    try:
        response = colecao.insert_many([dados])
        status   = response.acknowledged

        if status:
            message = f"Sucesso, {len(response.inserted_ids)} dados inseridos"
        else:
            message = "Erro ao inserir"

    except pymongo.errors as E:
        message = str(E)
        status = False

    return (status, message)

def update(aeroporto, nomeColecao:str, filter:dict, pattern:dict) -> tuple:
    """
    Função que atualiza dados no DB com base num filtro
    Recebe um filtro e as modificações que devem ser feitas
    Retorna uma tupla contendo um int que indica quantos valores foram alterados
        e uma mensagem de resposta
    """
    colecao  = aeroporto[nomeColecao]

    try:
        response = colecao.update_many(filter, {"$set": pattern}, True)
        total    = response.modified_count

        if total == 0:
            message = "Nenhuma entrada foi modificada"
        else:
            message = f"{total} entradas foram modificadas"

    except pymongo.errors as E:
        message = str(E)
        total   = -1

    return (total, message)

def delete(aeroporto, nomeColecao:str, filter:dict) -> tuple:
    """
    Função que deleta dados no DB com base num filtro
    Recebe um filtro que indica quais dados devem ser deletados
    Retorna uma tupla contendo um int que indica quantos valores foram deletados
        e uma mensagem de resposta
    """
    colecao  = aeroporto[nomeColecao]

    try:
        response = colecao.delete_many(filter)
        total    = response.deleted_count

        if total == 0:
            message = "Nenhuma entrada foi deletada"
        else:
            message = f"{total} entradas foram deletadas"

    except pymongo.errors as E:
        message = str(E)
        total   = -1

    return (total, message)
