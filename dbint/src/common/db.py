import pymongo

class Database(object):
    #blueprint
    URI = "mongodb://docker.for.mac.host.internal:27017"
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