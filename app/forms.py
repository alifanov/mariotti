from django import forms
from app.models import *

class ContactPageForm(forms.ModelForm):
    class Meta:
        model = ContactFormApply