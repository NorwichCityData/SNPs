'''
A collection of functions to deal with file housekeeping
'''
from django.conf import settings
import uuid
import os
import datetime
from .mongo import edit_file_record
from threadlocals.threadlocals import get_current_request
from settings import NOUNS

def handle_uploaded_file(form, user_id):

    f = form.files['file']
    # save file to disk
    f_name = str(uuid.uuid4()) + '.part'
    with open(os.path.join(settings.MEDIA_ROOT, f_name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    # now create db record for file
    fields = dict()
    fields['name'] = f_name
    fields['orig_name'] = f._name
    fields['size_in_bytes'] = f._size
    fields['uploaded_on'] = datetime.datetime.now()
    fields['notes'] = form.data['notes']
    fields['user_reference'] = form.data['reference']
    fields['user'] = user_id
    edit_file_record(fields, NOUNS['PUT'])

