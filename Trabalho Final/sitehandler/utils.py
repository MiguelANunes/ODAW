from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv
import dbconnection

def get_db_handle():
    """
    Inicializa a DB e retorna o objeto de conexão com o DB e a coleção do aeroporto 
    """

    # Source enviroment variables
    load_dotenv()

    # Get enviroment variables
    db_user = getenv('MONGODB_USER')
    db_passwd = getenv('MONGODB_PASSWD')
    db_cluster = getenv('MONGODB_CLUSTER')

    client = dbconnection.init_connection("mongodb+srv://"+db_user+":"+db_passwd+"@"+db_cluster+".kmhfvzx.mongodb.net/?retryWrites=true&w=majority")
    aeroporto = client['Aeroporto']
    
    return (client, aeroporto)

def close_db_handle(client):
    
    if not dbconnection.close_conection(client):
        exit()