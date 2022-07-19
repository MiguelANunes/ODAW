# Aqui vai ficar a conectividade com o banco de dados

# pip install pymongo
# https://pymongo.readthedocs.io/en/stable/
# pip install dnspython
# https://www.dnspython.org/

# https://www.mongodb.com/languages/python


import psycopg2, sys, datetime
import pymongo, pymongo.errors

def init_connection():
    """
    Função que começa a conexão com o banco de dados
    Retorna o objeto de conexão com o banco caso teve sucesso, retorna False otherwise
    """

    try:        
        client = pymongo.MongoClient("mongodb+srv://usuario:funcao235@cluster0.kmhfvzx.mongodb.net/?retryWrites=true&w=majority")
    except pymongo.errors.ConnectionFailure as E:
        print(E)
        print("Erro ao iniciar a conexão", file=sys.stderr)
        return False

    # isso me retorna a database "Aeroporto" na conexão
    return client['Aeroporto']

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

def find():
    # TODO
    pass

def insert(conn, tablename:str, values:tuple):
    """
    Função para inserir dados nas tabelas
    Retorna quantos valores foram inseridos, se conseguiu inserir,
    Se não, retorna None
    """

    execString = f"insert into {tablename} values {values}"

    results = execute_query(conn, execString, False)

    return results

def update(conn, tablename:str, fields:list, newvalues:list, wherecond:str):
    """
    Função para atualizar dados nas tabelas
    Retorna quantos valores foram modificados, se conseguiu modificar,
    Se não, retorna False
    """

    # field e newvalue são listas de, respectivamente, atributos e os valores novos p/ esses atributos

    wherecond = 'where ' + wherecond

    if len(fields) != len(newvalues):
        print("Erro no update, qtd de campos e novos valores é diferente", file=sys.stderr)
        return None

    setstring = ""
    try:
        for field, value in zip(fields, newvalues):
            setstring += f"set {field} = {value}"
    except TypeError:
        print("Erro ao fazer update", file=sys.stderr)
        return None

    execString = f"update {tablename} {setstring} {wherecond}"

    results = execute_query(conn, execString, False)

    return results

def delete(conn, tablename:str, wherecond:str):
    """
    Função para deletar dados nas tabelas
    Retorna True se conseguiu deletar, False se não
    """

    wherecond = 'where ' + wherecond
    execString = f"delete from {tablename} {wherecond}"

    results = execute_query(conn, execString, False)

    return results

def user_query_select(conn, query:str):
    """
    Função para executar um select do usuário
    Retorna False se não conseguiu rodar, retorna o que a query retornou se conseguiu
    """
    results = execute_query(conn, query, True)
    return results

def user_query_other(conn, query:str):
    """
    Função para executar uma query qualquer do usuário que não é um select
    Retorna False se não conseguiu rodar, retorna o que a query retornou se conseguiu
    """
    results = execute_query(conn, query, False)
    return results

def execute_query(conn, execString:str, returnsTable:bool):
    """
    Função para executar uma query 
        Já que praticamente todas as funções acima lidam com a execução de uma 
        query de praticamente a mesma forma, é mais conveniente colocar isso 
        numa função separada
    execString é a query a ser executada
    returnsTable indica se essa query deveria retornar tabelas ou não, i.e.:
        True:  Retorna tabelas     (usa o método fetchall())
        False: Não retorna tabelas (usa o método rowcount())
    """

    try:
        with conn.cursor() as mycursor:
            mycursor.execute(execString)
            conn.commit()

            if returnsTable:
                results = mycursor.fetchall() # retorna uma lista de tuplas
            else:
                results = mycursor.rowcount

    except psycopg2.ProgrammingError as E: # Erro gerado caso a query de erro
        print(E)
        print("Erro ao executar a query",execString, file=sys.stderr)
        return None

    return results