#!/usr/bin/env python3
"""
Module that provides a function to filter schools by a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo
            collection object.
        topic (str): The topic searched within the 'topics' attribute.

    Returns:
        list: A list of school documents that include the given topic.
    """
    return list(mongo_collection.find({"topics": topic}))