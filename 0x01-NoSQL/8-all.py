#!/usr/bin/env python3
'''Module to list all documents in a collection.'''


def list_all(mongo_collection):
    '''Lists all documents in a collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        List of documents or an empty list if no document is found.
    '''
    if mongo_collection is None:
        return []

    documents = mongo_collection.find()
    return list(documents)
