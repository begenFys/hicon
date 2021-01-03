from django.shortcuts import render, redirect
from django.contrib.auth.models import User
""" from .models import Info
from .forms import InfoForm """

def account(request):
  person = User.objects.get(id=request.user.id)
  """ person_info = Info.objects.get(email=request.user.email) """
  context = {
      'acc' : person,
  }
  return render(request, 'account/account.html', context)
"""   if request.method == 'POST':
    form = InfoForm(request.POST or None)
    if form.is_valid():
      Info.objects.filter(id=person_info.id).update(
        number_class = form.cleaned_data['number_class'],
        fav_subj = form.cleaned_data['fav_subj'],
        info = True
      )
      person_info.refresh_from_db()
      return redirect('account')
  else:
    form = InfoForm()
    context = {
      'acc' : person,
      'acc_info': person_info,
      'form' : form
    } """