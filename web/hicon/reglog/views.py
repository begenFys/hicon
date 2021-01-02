from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegForm, LoginForm
from django.contrib.auth import authenticate, login

def reg(request):
  if request.method == 'POST':
    form_reg = RegForm(request.POST or None)
    if form_reg.is_valid():
      new_user = User.objects.create(
        username = form_reg.cleaned_data['email'],
        email = form_reg.cleaned_data['email'],
        first_name = form_reg.cleaned_data['first_name'],
        last_name = form_reg.cleaned_data['last_name'],
        password = form_reg.cleaned_data['password']
      )
      user = authenticate(username=form_reg.cleaned_data['email'], email=form_reg.cleaned_data['email'], password=form_reg.cleaned_data['password'])
      login(request, user)
      print('work')
      return redirect('account')

    context = {
    'form': form_reg,
    }

    return render(request, 'reglog/reg.html', context)
  
  else:
    form_reg = RegForm()
    context = {
      'form': form_reg
    }
    return render(request, 'reglog/reg.html', context)

def log(request):
  if request.method == 'POST':
    form_log = LoginForm(request.POST or None)
    if form_log.is_valid():
      email = form_log.cleaned_data['email']
      password = form_log.cleaned_data['password']
      user = authenticate(username=email, email=email, password=password)
      if user:
        login(request, user)
        return redirect('account')
      
    context = {
      'form': form_log,
    }

    return render(request, 'reglog/log.html', context)
  
  else:
    form_log = LoginForm()
    context = {
    'form': form_log,
    }
    return render(request, 'reglog/log.html', context)
