from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def promo(request):
  try:
    user = User.objects.get(id=request.user.id)
  except:
    return render(request, 'promo/promo.html')
  else:
    return redirect('account')