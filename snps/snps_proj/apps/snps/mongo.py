__author__ = 'felixshaw'
import pymongo
from bson import ObjectId
from settings import NOUNS
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


def file_record(task, target_id = None, fields=None):
    if task == NOUNS['GET']:
        # we are dealing with a simple get
        if target_id:
            return get_collection_handle('file').find_one({'_id': target_id})
        else:
            raise AttributeError('Target ID not supplied to GET Operation.')
    elif task == NOUNS['PUT']:
        if target_id and fields:
            # we are dealing with an update
            record = get_collection_handle('file').find_one({'_id': target_id})
            record['snps'] = fields
            return get_collection_handle('file').update({'_id': target_id}, {"$set":record})
        elif fields:
            # we are dealing with a new record
            doc = get_collection_handle('file').insert(fields)
            return doc
        else:
            raise AttributeError('Either target_id or fields not supplied to PUT operation.')
    elif task == NOUNS['DELETE']:
        # we mark the record as deleted
        if target_id:
            return get_collection_handle('field').update({'_id': target_id, 'deleted': 1})
        else:
            raise AttributeError('No target_id supplied to delete operation.')


def get_file_records_for_user(user_id):
    docs = get_collection_handle('file').find({'user': user_id}, {"_id": 0, 'snps': 0})
    return docs