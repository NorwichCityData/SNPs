__author__ = 'felixshaw'
import pymongo
from bson import ObjectId

from django.conf import settings


def get_collection_ref(collection_name):
    return pymongo.MongoClient(settings.MONGO["host"], settings.MONGO["port"])[settings.MONGO["database"]][collection_name]


def to_mongo_id(id):
    return ObjectId(id)

def cursor_to_list(cursor):
    records = []
    for r in cursor:
        records.append(r)
    return records


fileReference = 'fileCollection'

handle_dict = dict(
    file=get_collection_ref(fileReference)
)


def get_collection_handle(component):
    return handle_dict.get(component)


def edit_file_record(fields, task, target_id = None,):
    if task == 'get':
        # get the record
        pass
    elif task == 'put':
        if target_id:
            # edit the existing record
            pass
        else:
            # we are dealing with a new record
            doc = get_collection_handle('file').insert(fields)
            return doc


def get_file_records_for_user(user_id):
    docs = get_collection_handle('file').find({'user': user_id}, {"_id": 0})
    return docs