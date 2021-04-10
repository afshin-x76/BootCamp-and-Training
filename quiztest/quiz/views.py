from django.shortcuts import render
from .models import Questions, Test, TestAnswers
from users.models import Student
from django.contrib.auth.decorators import login_required
import random
from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def answer_or_show_question(request, id):
    if request.method == 'POST':
        # get answer and add to test answers
        data = json.loads(request.body)

        test = Student.objects.get(user=request.user).test.get(status=True)
        
        question = test.questions.all()[id-1]
        testanswer = TestAnswers.objects.get_or_create(question=question, test=test)[0]
        testanswer.answer=data['answer']
        testanswer.save()

        question = test.questions.all()[id]

    elif request.method == 'GET':
        test = Student.objects.get(user=request.user).test
        question = test.questions.all()[id-1]

    # Generate random answers for next question
    answers = []
    temp_answers = [i.answer for i in question.wrong_answers.all()]
    temp_answers.append(question.right_answer)
    for i in temp_answers.copy():
        answer = random.choice(temp_answers)
        answers.append(answer)
        temp_answers.remove(answer)
    
    result = {
        "question": question.title,
        'answers': answers
    }
    return JsonResponse(result)

@login_required
def end_test(request):
    test = Student.objects.get(user=request.user).test
    test.status = False
    test.save()
    return HttpResponse("Test closed")

@login_required
def show_score(request):
    """
    always return the score of last test
    """
    test = Student.objects.get(user=request.user).test.all().reverse()[0]
    score = test.score
    return HttpResponse(f"Yor Score is {score}")

@login_required
def test(request):
    user = Student.objects.get(user=request.user)
    test = Test.objects.get_or_create(student=user, status=True)
    
    if 'questions' not in test:
        print("helloooooooooooooooooooooooo")
        # if there is no question for that test    
        questions = Questions.objects.all()
        qsts = []
        
        # copy the queryset into list
        # because queryset has no remove method
        questions_cop = []
        for i in questions:
            questions_cop.append(i)

        rand_qsts = []
        for i in range(5):
            qst = random.choice(questions_cop)
            rand_qsts.append(qst)
            questions_cop.remove(qst)
        test = test[0]
        print(test)
        test.questions.set(rand_qsts)

    question = test.questions.all()[0]

    # generate random answer for first question
    answers = []
    temp_answers = [i.answer for i in question.wrong_answers.all()]
    temp_answers.append(question.right_answer)
    for i in temp_answers.copy():
        answer = random.choice(temp_answers)
        answers.append(answer)
        temp_answers.remove(answer)

    print(answers)
    result = {
        "question": question.title,
        "answer": answers
    }
    return JsonResponse(result)


    
