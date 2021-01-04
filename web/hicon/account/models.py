from django.db import models

class Subjects(models.Model):
  name = models.CharField('Предмет', max_length=50)
  def __str__(self):
    return self.name
  class Meta:
    verbose_name = 'Предмет'
    verbose_name_plural = 'Предметы'

class ListHomework(models.Model):
  email = models.CharField('Email', max_length = 100)
  subj = models.ForeignKey(Subjects,verbose_name='Предмет', on_delete=models.CASCADE)
  homework = models.CharField('Дз', max_length=255)
  date = models.DateField('Дата сдачи')

  def __str__(self):
    return f'Дз {self.email} по {self.subj}'

  class Meta:
    verbose_name = 'Домашка'
    verbose_name_plural = 'Домашка'