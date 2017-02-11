'''
A collection of functions to deal with file housekeeping
'''
from django.conf import settings
import uuid
import os
import datetime
from .mongo import file_record
from threadlocals.threadlocals import get_current_request
from settings import NOUNS
import pandas as pd


# method to write uploaded file to media location and create mongo record
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
    return file_record(fields=fields, task=NOUNS['PUT'])



# method to parse excel spreadsheet and store data in existing record
def parse_spreadsheet_from_mongo_record(mongo_id):
    record = file_record(task=NOUNS['GET'], target_id=mongo_id)
    file_name = os.path.join(settings.MEDIA_ROOT, record['name'])

    xls_file = pd.ExcelFile(file_name)
    df = xls_file.parse("Sheet1", header=None)

    # get genes
    gene_df = pd.DataFrame(df.iloc[0:1, :])
    gene_df = gene_df.to_dict('records')
    gene_df = gene_df[0]


    # get rs
    rs_df = pd.DataFrame(df.iloc[1:2, :])
    rs_df = rs_df.to_dict('records')
    rs_df = rs_df[0]

    # get samples
    samples_df = pd.DataFrame(df.iloc[2:, :])

    def refactor_sample_record(x):
        sample_dict = dict(name=x[0])
        characteristics = list()

        for i in range(1, len(x)):
            characteristics.append(dict(gene=gene_df[i], rs=rs_df[i], snp=x[i]))

        sample_dict['characteristics'] = characteristics
        return sample_dict


    v = samples_df.apply(lambda row: refactor_sample_record(row), axis=1)
    return list(v)





