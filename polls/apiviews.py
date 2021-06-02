import uuid

from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Poll, Question, Answer, Vote
from .permissions import IsVoteOwnerOrAdmin
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class QuestionViewSet(NestedViewSetMixin, ModelViewSet):
    """questions ViewSet"""
    model = Question
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AnswerViewSet(NestedViewSetMixin, ModelViewSet):
    """answers ViewSet"""
    model = Answer
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VoteViewSet(NestedViewSetMixin, ModelViewSet):
    """votes ViewSet"""
    model = Vote
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsVoteOwnerOrAdmin]

    def perform_create(self, serializer):
        if 'user_uuid' not in self.request.session:
            self.request.session['user_uuid'] = str(uuid.uuid4())
        unique_id = self.request.session['user_uuid']
        serializer.validated_data['user'] = str(unique_id)
        answer_pk = self.kwargs['parent_lookup_answer']
        serializer.validated_data['answer'] = Answer.objects.get(pk=answer_pk)
        serializer.save()
