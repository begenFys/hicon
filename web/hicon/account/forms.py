from django import forms
""" from .models import Info


class InfoForm(forms.ModelForm):
  class Meta:
    model = Info 
    fields = ['number_class', 'fav_subj']
    widgets = {
      'number_class': forms.NumberInput(attrs={
        'placeholder' : 'Номер класса',
        'required' : True,
        'min' : 1,
        'max' : 12
      }),
      'fav_subj': forms.TextInput(attrs={
        'placeholder' : 'Любимый предмет',
        'required' : True
      })
    }
 """