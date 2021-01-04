from django.shortcuts import render, redirect
from django.contrib.auth.models import User
""" from .models import Info
from .forms import InfoForm """

def account(request):
  try:
    person = User.objects.get(id=request.user.id)
  except:
    return redirect('log')
  else:
    context = {
        'acc' : person,
    }
    return render(request, 'account/account.html', context)
