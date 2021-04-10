from django.urls import path
from users.views import login_page, sign_up, hello
from .views import test, answer_or_show_question, end_test, show_score

urlpatterns = [
    path('login/', login_page),
    path('signup/', sign_up),
    path('hello/', hello),
    path('test/', test),
    path('test/<int:id>/', answer_or_show_question),
    path('test/end/', end_test),
    path('test/score/', show_score),
]