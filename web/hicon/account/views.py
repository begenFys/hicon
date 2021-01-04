from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import ListHomeworkForm

def account(request):
  try:
    person = User.objects.get(id=request.user.id)
  except:
    return redirect('log')
  else:
    form = ''
    if request.method == 'POST':
      form = ListHomeworkForm(request.POST)
      if form.is_valid():
        new_hw = form.save(commit=False)
        new_hw.email = person.email
        new_hw.subj = form.cleaned_data['subj']
        new_hw.homework = form.cleaned_data['homework']
        new_hw.date = form.cleaned_data['date']
        new_hw.save()
        return redirect('account')  
    else:
      form = ListHomeworkForm()

    context = {
        'acc' : person,
        'form' : form
    }
    return render(request, 'account/account.html', context)
