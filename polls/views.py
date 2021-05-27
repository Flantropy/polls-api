from rest_framework import viewsets
from .models import Poll, Question
from .serializers import PollSerializer, QuestionSerializer
from rest_framework.permissions import IsAdminUser


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAdminUser]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]
