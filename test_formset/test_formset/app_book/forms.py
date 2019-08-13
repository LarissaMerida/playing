# forms.py :: part 1

from django import forms
from django.forms import formset_factory
from .models import *

class BookForm(forms.Form):
    name = forms.CharField(
        label='Book Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
        })
    )
BookFormset = formset_factory(BookForm, extra=1)

from django.forms import modelformset_factory

BookModelFormset = modelformset_factory(
    Book,
    fields=('name', 'casa', ),
    extra=1,
    widgets={'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
        })
    }
)