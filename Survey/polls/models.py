from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class TypeQA(models.Model):
    tpe = models.CharField('тип вопроса', max_length=256)

    def __str__(self):
        return self.tpe


class Question(models.Model):
    descriptionQA = models.CharField('текст вопроса', max_length=255, blank=True)
    typeQA = models.ForeignKey(TypeQA, on_delete=models.CASCADE)

    def __str__(self):
        return self.descriptionQA

    def choices(self):
        if not hasattr(self, '_choices'):
            self._choices = self.choice_set.all()
        return self._choices


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Polls(models.Model):
    title_p = models.CharField('Тема', max_length=56, blank=True)
    desc_p = models.CharField('Описание', max_length=255, blank=True)
    QA = models.ManyToManyField(Question, help_text="Вопросы", blank=True)
    s_date = models.DateTimeField()
    e_date = models.DateTimeField()

    def __str__(self):
        return self.title_p


class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voter = models.CharField(max_length=55, default=None)
