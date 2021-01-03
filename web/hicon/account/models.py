""" from django.db import models
from django.contrib.auth.models import UserManager

class Info(models.Model):
  email = models.EmailField('Email')
  number_class = models.PositiveIntegerField('Класс')
  fav_subj = models.CharField('Любимый предмет', max_length=30)
  info = models.BooleanField('Наличие', default=False)

  objects = UserManager()

  def __str__(self):
    return f'Информация о {self.email}'

  class Meta:
    verbose_name = 'Информация'
    verbose_name_plural = 'Информация' """
