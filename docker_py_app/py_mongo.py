import pprint
from pymongo import MongoClient
import sys


def create_mongo():
    # use when starting application locally
    # if you want to connect to local mongo instance. Not used here, just to mention
    mongoLocalUrl = "mongodb://admin:password@localhost:27017"

    # If this app runs in docker, use the name of the db container(mongodb) to connect to as both the app and
    # db are running in the same network. If the app runs in host and db in container then use the ip address of the
    # container to connect to.

    mongoDockerUrl = MongoClient("mongodb://admin:password@mongodb:27017")

    dbnames = mongoDockerUrl.list_database_names() # check if database already exists, then just return
    print(dbnames)
    if 'pydb' in dbnames:
        print("exiting py-app as db already exists:")
        return mongoDockerUrl, 0

    # try to instantiate a client instance
    new_db = mongoDockerUrl.pydb  # if database does not exist then mongodb creates one for you with name pydb
    return mongoDockerUrl, new_db


def create_collection_and_insert(dbname, list_elements):
    pyCollection = dbname.tutorial  # creates a collection named 'tutorial' if it does not exist
    for el in list_elements:
        result = pyCollection.insert_one(el)  # insert one element in the collection
        print(f"One tutorial: {result.inserted_id}")
    return pyCollection

    # You can also insert multiple elements at a time using insert_many()
    # new_result = pyCollection.insert_many([tutorial2, tutorial3])    # insert multiple elements in the collection atonce


def get_collection(collection):
    for doc in collection.find():
        pprint.pprint(doc)


tutorial1 = {
    "title": "Working With JSON Data in Python",
    "author": "YK",
    "contributors": [
        "ak",
        "bk",
        "ck"
    ],
    "url": "https://realpython.com/python-json/"
}

tutorial2 = {
    "title": "Python's Requests Library (Guide)",
    "author": "TK",
    "contributors": [
        "dk",
        "ek",
        "fk"
    ],
    "url": "https://realpython.com/python-requests/"
}

tutorial3 = {
    "title": "Object-Oriented Programming (OOP) in Python 3",
    "author": "GK",
    "contributors": [
        "gk",
        "hk",
        "ik"
    ],
    "url": "https://realpython.com/python3-object-oriented-programming/"
}

tutorial = [tutorial1, tutorial2, tutorial3]  # list of tutorials to insert

if __name__ == '__main__':
    mongoDockerUrl, new_db_name = create_mongo()  # create a new db
    if new_db_name == 0:
        sys.exit()
    # create new collection and insert elements
    new_collection = create_collection_and_insert(new_db_name, tutorial)
    get_collection(new_collection)  # print the elements added
    mongoDockerUrl.close()
