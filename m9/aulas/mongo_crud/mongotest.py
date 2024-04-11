# Import the lib pymongo to manage sync data in db. 
from pymongo import MongoClient

# Connecting to db 
client = MongoClient('mongodb://localhost:27017/')
# Creating a collection
db = client['meu_banco']


# CRUD

# Inserting one/some docs
colecao = db['minha_colecao']
colecao.insert_one({'nome': 'João', 'idade': 30})
colecao.insert_many([{'nome': 'Maria', 'idade': 25}, {'nome': 'Pedro', 'idade': 35}])

# Searching for docs
for doc in colecao.find({'idade': {'$gt': 30}}):
    print(doc)

# Updating docs
colecao.update_one({'nome': 'João'}, {'$set': {'idade': 31}})

# Deleting docs
colecao.delete_one({'nome': 'Pedro'})

# Creating a TTL index
colecao.create_index([('data_criacao', 1)], expireAfterSeconds=3600)
#TTL indexes are special single-field indexes that MongoDB can use to automatically remove documents from a collection after a certain amount of time or at a specific clock time. Data expiration is useful for certain types of information like machine generated evment data, logs, and session information that only need to persist in a database for a finite amount of time.