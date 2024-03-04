from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30122
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
    
    # Inserts a document into the collection
    def create(self, data):
        if data is not None:
            try:
                self.database.animals.insert_one(data)  # data should be dictionary        
                return True
            except Exception as e:
                print(f"An error occurred during insert: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False
            
    # Queries documents based on a key/value pair
    def read(self, query):
        if query is not None:
            try:
                documents = self.collection.find(query)
                return list(documents)
            except Exception as e:
                print(f"An error occurred during read: {e}")
                return []
        else:
            return []

    # Updates documents based on a query and update values
    def update(self, query, update_values):
        if query is not None and update_values is not None:
            try:
                result = self.collection.update_many(query, {'$set': update_values})
                return result.modified_count
            except Exception as e:
                print(f"An error occurred during update: {e}")
                return 0
        else:
            return 0
    
    # Removes documents based on a query
    def delete(self, query):
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"An error occurred during delete: {e}")
                return 0
        else:
            return 0