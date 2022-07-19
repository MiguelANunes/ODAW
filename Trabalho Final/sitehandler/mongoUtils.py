# To import mongodb
import pymongo
import os
import dotenv

# get_database function

def get_database():
    # Source enviroment variables
    dotenv.load_dotenv()

    # Get enviroment variables
    db_user = os.getenv('MONGODB_USER')
    db_passwd = os.getenv('MONGODB_PASSWD')
    db_cluster = os.getenv('MONGODB_CLUSTER')

    # Set the connection URL and set mongo client
    conn_url = "mongodb+srv://"+db_user+":"+db_passwd+"@"+db_cluster+".kmhfvzx.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(conn_url)

    # Retrieve database "Aeroporto" from the client
    return client['Aeroporto']

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