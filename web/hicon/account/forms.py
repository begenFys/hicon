from django import forms
from .models import ListHomework, Matrix

class ListHomeworkForm(forms.ModelForm):
  class Meta:
    model = ListHomework
    fields = ['subj', 'homework', 'matrix_type','date']
    widgets = {
      "subj": forms.Select(attrs={
        'placeholder': 'Предмет',
        'required' : True
      }),
      "homework": forms.TextInput(attrs={
        'placeholder' : 'Домашка',
        'required' : True
      }),
      "matrix_type": forms.Select(attrs={
        'placeholder': 'Тип задания',
        'required' : True
      }),
      "date": forms.DateInput(attrs={
        'type' : 'date',
        'placeholder': 'На какое число задали',
        'required' : True
      }),
    }
  matrix_type = forms.ModelChoiceField(queryset=Matrix.objects.all(), to_field_name="type")