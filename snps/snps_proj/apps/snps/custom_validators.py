from django.core.exceptions import ValidationError

def validate_file_extension(value):
  import os
  ext = os.path.splitext(value.name)[1]
  valid_extensions = ['.xls','.xlsx','.csv']
  if not ext in valid_extensions:
    raise ValidationError(u'Please Upload Valid Excel Spreadsheet')