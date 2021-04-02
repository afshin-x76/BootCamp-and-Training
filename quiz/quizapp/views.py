from django.shortcuts import render
from .models import Questions, Student
from django.http import JsonResponse, HttpResponse
import random
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required



@csrf_exempt
def login_to_system(request):
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    body = json.loads(request.body)
    usename = body["username"]
    password = body["password"]
    user = authenticate(request, username=usename, password=password)
    if user is not None:
        login(request,user)
        return HttpResponse("login successfully")
    else:
        return HttpResponse("You Fucked Up...!")

def check(request):
    print(request.user)
    if request.user.is_authenticated:
        return HttpResponse("You are Authenticated")
    else:
        return HttpResponse("Get the Fuck OFF")


@login_required
def show_score(request):
    std = Student.objects.get(user=request.user)
    points = std.points
    print(points)
    score = points.count(1)
    return HttpResponse(f"Your score is {score}")


@csrf_exempt
@login_required
def show_questions(request, id):
    std = Student.objects.get(user=request.user)
    points = std.points
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(points)
    question = Questions.objects.all()
    if request.method == "POST":
        ans = json.loads(request.body)
        ans = ans["answer"]
        if ans == question[id-1].right_answer:
            points[id-1] = 1
        else:
            points[id-1] = 0
        std.points= points
        std.save()
        print(ans, question[id-1].right_answer)
        print(points)

        question = question[id]

        temp_answers = [question.right_answer, question.wrong_ansers]
        answers = []
        for i in range(2):
            answer = random.choice(temp_answers)
            answers.append(answer)
            temp_answers.remove(answer)
        
        content = {
            'question': question.question,
            'answer': answers
        }

        return JsonResponse(content)

    elif request.method == "GET":
        question = question[id-1]
        
        temp_answers = [question.right_answer, question.wrong_ansers]
        answers = []
        for i in range(2):
            answer = random.choice(temp_answers)
            answers.append(answer)
            temp_answers.remove(answer)
        
        content = {
            'question': question.question,
            'answer': answers
        }

        return JsonResponse(content)
    


