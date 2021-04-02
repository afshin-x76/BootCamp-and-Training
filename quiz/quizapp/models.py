from django.db import models
from django.contrib.auth.models import User
import json

class Questions(models.Model):
    question = models.CharField(max_length=300)
    right_answer = models.CharField(max_length=250)
    wrong_ansers = models.CharField(max_length=250)

    def __str__(self):
        return self.question
        
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.JSONField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
