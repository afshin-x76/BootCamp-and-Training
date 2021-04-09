from django.db import models
from django.contrib.auth.models import User


class BaseUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Student(BaseUser):
    pass

class Master(BaseUser):
    pass