# To import mongodb
import pymongo
import os
import dotenv
import dbconnection

# get_database function

def get_database() -> tuple:
    """
    Inicializa a DB e retorna o objeto de conexão com o DB e a coleção do aeroporto 
    """
    # Source enviroment variables
    dotenv.load_dotenv()

    # Get enviroment variables
    db_user = os.getenv('MONGODB_USER')
    db_passwd = os.getenv('MONGODB_PASSWD')
    db_cluster = os.getenv('MONGODB_CLUSTER')

    # Set the connection URL and set mongo client
    client = dbconnection.init_connection("mongodb+srv://"+db_user+":"+db_passwd+"@"+db_cluster+".kmhfvzx.mongodb.net/?retryWrites=true&w=majority")
    aeroporto = client['Aeroporto']
    
    return (client, aeroporto)

# Connect to the database using the get_database() function
db = get_database()

# Querying the "avioes" collection

# Set the collection
avioes_collection = db['avioes']

# Get collection documents
avioes = avioes_collection.find()

# Iterate over the documents
for aviao in avioes:
    print(aviao)