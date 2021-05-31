from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Poll, Question, Answer, Vote
from .serializers import (
    PollSerializer,
    QuestionSerializer,
    AnswerSerializer,
    VoteSerializer,
)


class PollViewSet(NestedViewSetMixin, ModelViewSet):
    """polls ViewSet"""
    model = Poll
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionViewSet(NestedViewSetMixin, ModelViewSet):
    """questions ViewSet"""
    model = Question
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(NestedViewSetMixin, ModelViewSet):
    """answers ViewSet"""
    model = Answer
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class VoteViewSet(NestedViewSetMixin, ModelViewSet):
    """votes ViewSet"""
    model = Vote
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
