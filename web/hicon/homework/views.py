from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from account.models import ListHomework
from .models import Notes
from .forms import NotesForm

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
    all_hw = ListHomework.objects.filter(email=person.email)
    type1 = []
    type2 = []
    type3 = []
    type4 = []
    type5 = []
    for i in all_hw:
      subj = i.subj.name
      homework = i.homework.split(';')
      matrix_type = i.matrix_type.split(';')
      date = i.date.split(';')
      for j in range(len(homework)):
        el = {
          'subj' : subj,
          'homework' : homework[j],
          'matrix_type' : matrix_type[j],
          'date' : date[j],
        }
        if el['matrix_type'][0] == '1':
          type1.append(el)
        elif el['matrix_type'][0] == '2':
          type2.append(el)
        elif el['matrix_type'][0] == '3':
          type3.append(el)
        elif el['matrix_type'][0] == '4':
          type4.append(el)
        else:
          type5.append(el)
    context = {
      'type1' : type1 or '',
      'type2' : type2 or '',
      'type3' : type3 or '',
      'type4' : type4 or '',
      'type5' : type5 or '',
    }
    return render(request, 'homework/matrix.html', context)

def notes(request):
  try:
    person = User.objects.get(id=request.user.id)
  except:
    return redirect('log')
  else:
    form = ''
    if request.method == 'POST':
      try:
        form = NotesForm(request.POST)
        notes = Notes.objects.get(email=person.email)
      except:
        if form.is_valid():
          new_notes = form.save(commit=False)
          new_notes.email = person.email
          new_notes.notes = form.cleaned_data['notes']
          new_notes.save()
          return redirect('account')  
      else:
        if form.is_valid():
          Notes.objects.filter(email=person.email).update(
            notes = form.cleaned_data['notes']
          )
          notes.refresh_from_db()
          return redirect('notes')
    else:
      try:
        obj = Notes.objects.get(email=person.email)
      except:
        form = NotesForm(
          initial={
            'notes': ''
          }
        )
      else:
        form = NotesForm(
          initial={
            'notes': obj.notes
          }
        )

    context = {
      'form': form,
      'text': obj.notes
    }
    return render(request, 'homework/notes.html', context)