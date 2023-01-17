#!/usr/bin/env python3
""" pymongo list """

import pymongo


def list_all(mongo_collection):
    """ List all elements in a collection """
    doc_list = []

    docs = mongo_collection.find()
    for doc in docs:
        doc_list.append(doc)

    return doc_list
