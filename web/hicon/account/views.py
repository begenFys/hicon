from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import ListHomeworkForm
from .models import ListHomework
from django.views.generic import DeleteView

def account(request):
  try:
    person = User.objects.get(id=request.user.id)
  except:
    return redirect('log')
  else:
    all_el = ListHomework.objects.filter(email=person.email)
    homeworks = []
    for el in all_el:
      homework = el.homework.split(';')
      homeworks.append([el.pk, el.subj.name, zip(homework, el.date.split(';'), [i for i in range(len(homework))])])

    if request.method == 'POST':
      try:
        form = ListHomeworkForm(request.POST)
        hw = ListHomework.objects.get(email=person.email, subj=form.data['subj'])
      except:
        if form.is_valid():
          new_hw = form.save(commit=False)
          new_hw.email = person.email
          new_hw.subj = form.cleaned_data['subj']
          new_hw.homework = form.cleaned_data['homework']
          cur_date = form.cleaned_data['date'].split('-')[::-1]
          new_hw.date = '.'.join(cur_date)
          new_hw.save()
          return redirect('account')  
      else:
        old_hw = hw.homework
        old_date = hw.date
        cur_date = form.data['date'].split('-')
        new_date = '.'.join(cur_date[::-1])
        ListHomework.objects.filter(subj=hw.subj).update(
          homework = old_hw + ';' + form.data['homework'],
          date = old_date + ';' + new_date
        )
        hw.refresh_from_db()
        return redirect('account')
    else:
      form = ListHomeworkForm()

    context = {
        'acc' : person,
        'form' : form,
        'homeworks' : homeworks
    }
    return render(request, 'account/account.html', context)

class CompleteHomework(DeleteView):
  model = ListHomework
  template_name = 'account/complete.html'
  success_url = '/account/'
  def delete(self, request, *args, **kwargs):
    path = request.path.split('/')
    pk = int(path[3])
    index = int(path[4])
    obj = ListHomework.objects.get(pk=pk)
    cur_hw = obj.homework.split(';')
    cur_hw.pop(index)
    if len(cur_hw)==0:
      obj.delete()
      return redirect('account')
    ListHomework.objects.filter(pk=pk).update(
      homework = ';'.join(cur_hw)
    )
    obj.refresh_from_db()
    return redirect('account')
