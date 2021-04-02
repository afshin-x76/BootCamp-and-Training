from django.urls import path
from .views import show_questions, login_to_system, check, show_score

urlpatterns = [
    path('<int:id>/', show_questions),
    path('login/', login_to_system),
    path("check/", check),
    path("score/", show_score)
]