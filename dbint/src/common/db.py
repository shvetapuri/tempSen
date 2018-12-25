import pymongo
import os
from pymongo import ReturnDocument

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
        seq = Database.getNextSequence('counters', 'userid')
        data['seq'] = seq
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find()

    @staticmethod
    def getNextSequence(collection, name):
        ret = Database.DATABASE[collection].find_one_and_update({'_id':name}, {'$inc': {'seq': 1}}, return_document=ReturnDocument.AFTER)
        print(ret)
        return ret['seq'] 

#gets first element stored in database
    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)