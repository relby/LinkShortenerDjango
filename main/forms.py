from django import forms
from django.forms.fields import URLField

class CreateLink(forms.Form):
    url = URLField(label="URL", max_length=2500)