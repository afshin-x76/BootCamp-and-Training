from django.db import models
from users.models import Student

class WrongAnswers(models.Model):
    answer = models.CharField(max_length=300)


class Questions(models.Model):
    title = models.CharField(max_length=250)
    right_answer = models.CharField(max_length=300)
    wrong_answers = models.ForeignKey(WrongAnswers,null=True ,blank=True , on_delete=models.SET_NULL)


class TestAnswers(models.Model):
    answer = models.CharField(max_length=300)


class Test(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Questions)
    answers = models.ForeignKey(TestAnswers, null=True, blank=True, on_delete=models.SET_NULL)