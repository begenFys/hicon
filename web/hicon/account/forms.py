from django import forms
from .models import ListHomework

class ListHomeworkForm(forms.ModelForm):
  class Meta:
    model = ListHomework
    fields = ['subj', 'homework', 'date']
    widgets = {
      "subj": forms.Select(attrs={
        'placeholder': 'Предмет',
        'required' : True
      }),
      "homework": forms.TextInput(attrs={
        'placeholder' : 'Домашка',
        'required' : True
      }),
      "date": forms.DateInput(attrs={
        'type' : 'date',
        'placeholder': 'На какое число задали',
        'required' : True
      }),
    }