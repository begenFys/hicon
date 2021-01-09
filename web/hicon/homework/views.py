from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def homework(request):
  try:
    person = User.objects.get(id=request.user.id)
  except:
    return redirect('log')
  else:
    return render(request, 'homework/homework.html')

def pomodoro(request):
  try:
    person = User.objects.get(id=request.user.id)
  except:
    return redirect('log')
  else:
    return render(request, 'homework/pomodoro.html')

def matrix(request):
  try:
    person = User.objects.get(id=request.user.id)
  except:
    return redirect('log')
  else:
    return render(request, 'homework/matrix.html')

def frog(request):
  try:
    person = User.objects.get(id=request.user.id)
  except:
    return redirect('log')
  else:
    return render(request, 'homework/frog.html')

def salami(request):
  try:
    person = User.objects.get(id=request.user.id)
  except:
    return redirect('log')
  else:
    return render(request, 'homework/salami.html')