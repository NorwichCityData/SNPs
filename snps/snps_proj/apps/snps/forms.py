from django import forms
from django.forms.widgets import Textarea


class UploadFileForm(forms.Form):
    reference = forms.CharField(label="Your Reference for this File", max_length=50)
    notes = forms.CharField(label="Pertinent Notes", required=False, widget=Textarea())
    file = forms.FileField(label="")
