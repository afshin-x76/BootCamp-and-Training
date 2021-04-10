from django.shortcuts import render
from .models import BaseUser, Student
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt 
import json
from django.http.response import HttpResponse


def hello(request):
    return HttpResponse("Hello man")

@csrf_exempt
def login_page(request):
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        print(data['username'])
        print(data['password'])
        user = authenticate(username=data['username'], password=data['password'])
        print(user)
        if user != None:
            login(request, user)
            return HttpResponse('Login Successful')
        else:
            return HttpResponse('You Are Not Authenticated')
    return HttpResponse('Use Post method')


@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        email = data['email']
        pas = data['password']
        user = User.objects.create_user(username, email, pas)

        return HttpResponse("Signup Successfull")

        


    




