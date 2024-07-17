#!/usr/bin/env python3
'''Module to insert a new document in a collection based on kwargs.'''


def insert_school(mongo_collection, **kwargs):
    '''Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Additional key-value pairs for the new document.

    Returns:
        The _id of the new document.
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
