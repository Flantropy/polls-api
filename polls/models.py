from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    title = models.CharField(max_length=100, unique=True, default='Poll Title')
    description = models.CharField(max_length=500, default='Describe your poll here')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    starts_on = models.DateField(auto_now_add=True)
    expires_on = models.DateField(null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500, default='Propose some question')

    class AnswerType(models.TextChoices):
        REGULAR = ('regular', 'one answer')
        MULTIPLE = ('multiple', 'few answers')
        TEXT = ('text', 'user input')

    expected_answer_type = models.CharField(max_length=20, choices=AnswerType.choices)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.answer_text


# TODO  resolve unique user id problem
# noinspection PyCallingNonCallable
class Vote(models.Model):
    answer = models.ForeignKey(Answer, related_name='votes', editable=False,
                               on_delete=models.CASCADE)
    # voted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # question = models.ForeignKey(Question, related_name='votes', on_delete=models.CASCADE)
    user = models.CharField(max_length=50, editable=False)
    user_input = models.CharField(max_length=300, default='')

    def __str__(self):
        vote = self.answer if not self.user_input else self.user_input
        return f'{self.user} voted for {vote}'
