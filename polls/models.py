from django.db import models
from django.contrib import auth
from django.utils import timezone
import random

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return "%s" % (self.id)

class Question(models.Model):
    id_q = models.AutoField(primary_key=True)
    name_question = models.CharField(max_length=50, default='void')
    text_question = models.TextField(max_length=1000)
    correct = models.BooleanField(default=False)
    def __str__(self):
        return "%s, normal:%s" % (self.name_question, self.correct)
    def random_question(self, exp):
        question_list = Question.objects.all()
        question_list = question_list.exclude(id_q__in=exp.values("question_id"))
        question_list = question_list.order_by('id_q')
        number = random.randint(0, question_list.count()-1)
        return question_list[number]

class Experiment(models.Model):
    user_id = models.ForeignKey(User)
    question_id = models.ForeignKey(Question)
    adequacy = models.IntegerField(default=1)
    answer = models.CharField(max_length=500, default="Ответ")
    time_start = models.IntegerField(default=0)
    def __str__(self):
        return "%s with answer %s" % (self.question_id, self.answer)
