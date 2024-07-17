#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Accessing the collection 'school' in the 'my_db' database
    school_collection = client.my_db.school

    # Fetching all documents in the collection
    schools = list_all(school_collection)

    # Printing the documents
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
