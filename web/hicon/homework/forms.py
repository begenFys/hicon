from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
  class Meta:
    model = Notes
    fields = ['notes']
    widgets = {
      "notes": forms.Textarea(attrs={
        'placeholder': 'Пиши всё что хочешь! Вот там Галина Валерьевна такая... мы всё оставим в секрете...',
        'class': 'notes__area'
      })
    }