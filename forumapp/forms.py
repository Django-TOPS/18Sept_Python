from dataclasses import fields
from pyexpat import model
from django import forms
from .models import signupMaster, notesMaster

class SignupForm(forms.ModelForm):
    class Meta:
        model=signupMaster
        fields='__all__'


class NotesForm(forms.ModelForm):
    class Meta:
        model=notesMaster
        fields='__all__'