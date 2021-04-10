from django.contrib import admin
from .models import Questions, TestAnswers, Test, WrongAnswers

admin.site.register(Questions)
admin.site.register(WrongAnswers)
admin.site.register(Test)
admin.site.register(TestAnswers)

