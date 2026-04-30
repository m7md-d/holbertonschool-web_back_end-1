#!/usr/bin/env python3
"""
Module for listing all documents in a MongoDB collection.

This module provides a utility function to interact with a MongoDB
collection using pymongo and retrieve all its documents as a list.
"""

def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection: A pymongo collection object.

    Returns:
        A list of all documents in the collection, or an empty list if none found.
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find())
