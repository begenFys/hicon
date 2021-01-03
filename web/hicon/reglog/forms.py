from django import forms
from django.contrib.auth.models import User


class RegForm(forms.ModelForm):
  def clean(self):
    email = self.cleaned_data['email']
    if User.objects.filter(email=email).exists():
      raise forms.ValidationError('Данный почтовый адрес уже зарегистрирован')
    return self.cleaned_data

  class Meta:
    model = User  
    fields = ['first_name', 'last_name', 'email','password']
    widgets = {
      'first_name': forms.TextInput(attrs={
        'placeholder' : 'Имя',
        'required' : True
      }),
      'last_name': forms.TextInput(attrs={
        'placeholder' : 'Фамилия',
        'required' : True
      }),
      'email': forms.EmailInput(attrs={
        'placeholder' : 'Email',
        'required' : True
      }),
      'password': forms.PasswordInput(attrs={
        'placeholder' : 'Пароль',
        'required' : True
      })
    }

class LoginForm(forms.ModelForm):
  def clean(self):
    email = self.cleaned_data['email']
    password = self.cleaned_data['password']
    if not User.objects.filter(email=email).exists():
      raise forms.ValidationError(f'Пользователь с таким email не найден')
    user = User.objects.filter(email=email).first()
    if user:
      if not user.check_password(password):
        raise forms.ValidationError('Неверный пароль')

    return self.cleaned_data

  class Meta:
    model = User
    fields = ['email', 'password']
    widgets = {
      'email': forms.EmailInput(attrs={
        'placeholder' : 'Email',
        'required' : True
      }),
      'password': forms.PasswordInput(attrs={
        'placeholder' : 'Пароль',
        'required' : True
      })
    }

     