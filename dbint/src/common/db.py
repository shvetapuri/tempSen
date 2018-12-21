import pymongo
import os

class Database(object):
    #blueprint
    dbhost = os.getenv('MONGO_HOST', "127.0.0.1")
    URI = "mongodb://" + dbhost + ":27017"
    DATABASE = None
    #will not use self in this method this method will belong to database class as a whole
    #never to instance of a database
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        #self is objects value, if we have static var then have to use classname.var
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection,data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find()

#gets first element stored in database
    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)