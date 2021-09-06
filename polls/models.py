from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    """
    Poll is creating by superuser, serves as root node for other models
    and can have any number of questions.
    """
    title = models.CharField(max_length=100, unique=True, default='Poll Title')
    description = models.CharField(max_length=500, default='Describe your poll here')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    starts_on = models.DateField(auto_now_add=True)
    expires_on = models.DateField(null=True)

    def __str__(self):
        return self.title


class Question(models.Model):

    """
    Question is creating by superuser, it's bound to particular poll,
    can have any number of answers and sets type of expected answer.
    """
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
    """
    Answer is creating by superuser, and serves as variant for it's question.
    If question expects answer of type AnswerType.TEXT, 'answer_text' field should be
    set to 'user input'.
    """
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.answer_text


class Vote(models.Model):
    """
    Vote can store key of answer voted by user, or 'user input'
    depending on answer type expected for question.
    """
    answer = models.ForeignKey(Answer, related_name='votes', editable=False,
                               on_delete=models.CASCADE)
    user = models.CharField(max_length=50, editable=False)
    user_input = models.CharField(max_length=300, default='')

    def __str__(self):
        vote = self.answer if not self.user_input else self.user_input
        return f'{self.user} voted for {vote}'
