from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
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
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33618
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("Connected to Database")

# Create Method for C in CRUD
    def create(self, data):
        if data is not None: # Checks if there is data
            try:
                insert = self.database.animals.insert_one(data)  # Inserts data into document
                return insert.acknowledged  # Returns true if successful
            except Exception as e:
                print("Error inserting into document:", e)
                return False # Sets to false and print error message
        else:
            print("No data inserted, invalid format")
            return False # Sets to false and print error message

# Read Method for R in CRUD
    def read(self, searchData):
        if searchData: # Searches for matching data within document
            data = self.database.animals.find(searchData, {"_id": False}) # excludes false in the ID field
        else:
            data = self.database.animals.find( {}, {"_id": False})
        return data
    
# Update Method for U in CRUD
    def update(self, query, updateData, multiple=False):
        if query and updateData:
            try:
                if multiple: # Updates multiple entries with new data
                    result = self.database.animals.update_many(query, {'$set': updateData})
                else: # Updates single entry with new data
                    result = self.database.animals.update_one(query, {'$set': updateData})
                return result.modified_count # Number of results modified
            except Exception as e:
                print("Error updating document:", e)
                return 0 # Sets to 0 and print error message
        else:
            print("Invalid update format")
            return 0 # Sets to 0 and print error message

# Delete Method for D in CRUD
    def delete(self, query, multiple=False):
        if query:
            try:
                if multiple: # Removes multiple entries
                    result = self.database.animals.delete_many(query)
                else: # Removes single entry
                    result = self.database.animals.delete_one(query)
                return result.deleted_count # Number of results removed
            except Exception as e:
                print("Error deleting document:", e)
                return 0 # Sets to 0 and print error message
        else:
            print("Invalid delete format")
            return 0 # # Sets to 0 and print error message