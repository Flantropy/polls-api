from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    title = models.CharField(max_length=100, unique=True, default='Poll Title')
    description = models.CharField(max_length=500, default='Describe your poll here')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    starts_on = models.DateField(auto_now_add=True)
    expires_on = models.DateField(null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    class AnswerType(models.TextChoices):
        REGULAR = ('R', 'one answer')
        MULTIPLE = ('M', 'few answers')
        TEXT = ('T', 'user input')

    question_text = models.CharField(max_length=500, default='Propose some question')
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    expected_answer_type = models.CharField(max_length=8, choices=AnswerType.choices)
    answer_variant_1 = models.CharField(max_length=200, default='answer example')
    answer_variant_2 = models.CharField(max_length=200, default='answer example')
    answer_variant_3 = models.CharField(max_length=200, default='answer example')
    answer_variant_4 = models.CharField(max_length=200, default='answer example')

    def __str__(self):
        return self.question_text
