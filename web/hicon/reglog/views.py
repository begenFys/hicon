from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegForm, LoginForm
""" from account.models import Info """
from django.contrib.auth import authenticate, login

def reg(request):
  try:
    user = User.objects.get(id=request.user.id)
  except:
    if request.method == 'POST':
      form_reg = RegForm(request.POST)
      if form_reg.is_valid():
        new_user = form_reg.save(commit=False)
        new_user.username = form_reg.cleaned_data['email']
        new_user.email = form_reg.cleaned_data['email']
        new_user.first_name = form_reg.cleaned_data['first_name']
        new_user.last_name = form_reg.cleaned_data['last_name']
        new_user.save()
        new_user.set_password(form_reg.cleaned_data['password'])
        new_user.save()
        login(request, new_user)
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
  else:
    return redirect('account')

def log(request):
  try:
    user = User.objects.get(id=request.user.id)
  except:
    if request.method == 'POST':
      form_log = LoginForm(request.POST or None)
      if form_log.is_valid():
        email = form_log.data['email']
        password = form_log.data['password']
        user = authenticate(username=email, email=email, password=password)
        if user is not None:
          login(request, user)
          return redirect('account')
        
      context = {
        'form': form_log
      }

      return render(request, 'reglog/log.html', context)
  
    else:
      form_log = LoginForm()
      context = {
      'form': form_log,
      }
      return render(request, 'reglog/log.html', context)

  else:
    return redirect('account')
