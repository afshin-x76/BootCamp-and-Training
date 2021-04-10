from django.contrib import admin
from .models import Student, Master, BaseUser

admin.site.register(BaseUser)
admin.site.register(Student)
admin.site.register(Master)
