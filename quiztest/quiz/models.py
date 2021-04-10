from django.db import models
from users.models import Student

class Questions(models.Model):
    title = models.CharField(max_length=250)
    right_answer = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class WrongAnswers(models.Model):
    answer = models.CharField(max_length=300)
    question = models.ForeignKey(Questions,null=True, on_delete=models.CASCADE, related_name='wrong_answers')

    def __str__(self):
        return self.answer


class Test(models.Model):
    status = models.BooleanField(default=True) # represent that this test is open or closed
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='test', related_query_name='tests')
    questions = models.ManyToManyField(Questions)

    def __str__(self):
        return self.student.name

    @property
    def score(self):
        score = 0
        for answer in self.answers.all():
            if answer.get_score():
                score += 1
        return score

class TestAnswers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=300, null=True, blank=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.question.title

    def get_score(self):
        if self.answer == self.question.right_answer:
            return True
        return False