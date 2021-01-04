from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def homework(request):
  try:
    person = User.objects.get(id=request.user.id)
  except:
    return redirect('log')
  else:
    return render(request, 'homework/homework.html')