"""
Module that provides a function to insert a document into a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo 
            collection object.
        **kwargs: Arbitrary keyword arguments representing the document 
            attributes.

    Returns:
        The new _id of the inserted document.
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id