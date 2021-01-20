from django.db import models

class Notes(models.Model):
  email = models.CharField('Email', max_length = 100)
  notes = models.TextField('Заметки')

  def __str__(self):
    return f'Заметки {self.email}'

  class Meta:
    verbose_name = 'Заметки'
    verbose_name_plural = 'Заметки'