from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=100, default='')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    description = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['start_date']


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.question_text

    class Meta:
        ordering = ['poll']
