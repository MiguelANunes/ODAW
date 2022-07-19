from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

def get_db_handle():
    # Source enviroment variables
    load_dotenv()

    # Get enviroment variables
    db_user = getenv('MONGODB_USER')
    db_passwd = getenv('MONGODB_PASSWD')
    db_cluster = getenv('MONGODB_CLUSTER')

    # Set the connection URL and set mongo client
    conn_url = "mongodb+srv://"+db_user+":"+db_passwd+"@"+db_cluster+".kmhfvzx.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(conn_url)

    db_handle = client['Aeroporto']

    return db_handle, client
