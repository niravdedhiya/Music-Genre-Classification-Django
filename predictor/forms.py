from django import forms
from .models import Document

class DocumentForm(forms.Form):
    def is_valid(*args, **kwargs):
        return True

    file = forms.FileField(help_text='Valid .mp3 file')
