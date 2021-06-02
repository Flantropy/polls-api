import uuid

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user
from django.http import HttpResponse
from django.urls import reverse
from django.utils.timezone import now
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Poll, Question, Answer, Vote
from .serializers import (
    PollSerializer,
    QuestionSerializer,
    AnswerSerializer,
    VoteSerializer,
)


# TODO [?] add custom POST action for sending all user votes/answers for particular poll
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

    def perform_create(self, serializer):
        if 'user_uuid' not in self.request.session:
            self.request.session['user_uuid'] = str(uuid.uuid4())
        unique_id = self.request.session['user_uuid']
        serializer.validated_data['user'] = str(unique_id)
        answer_pk = self.kwargs['parent_lookup_answer']
        serializer.validated_data['answer'] = Answer.objects.get(pk=answer_pk)
        serializer.save()

    # @action(methods=['GET', 'POST'], detail=False)
    # def do_vote(self, request: Request, *args, **kwargs):
    #     print(f'uuid = {request.session["user_uuid"]}')
    #     print(self.kwargs['parent_lookup_answer'])
    #     return super().list(request)

    # def create(self, request, *args, **kwargs):
    #     user = get_user(request)
    #     if isinstance(user, AnonymousUser):
    #         return HttpResponse(status=status.HTTP_403_FORBIDDEN)
    #     return super().create(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     user = get_user(request)
    #     if isinstance(user, AnonymousUser):
    #         self.permission_classes = ()
    #         self.authentication_classes = ()
    #         self.queryset.filter('expires_on' < str(now()))
    #         print('welcome in the club')
    #         self.request.user.id = 3243
    #     elif user.is_superuser:
    #         print('hi master')
    #
    #     print(request.session.session_key)
    #     print(request.user.id)
    #     return super().list(request, *args, **kwargs)
    #
    # @action(methods=['GET'], detail=False)
    # def do_something(self, request, *args, **kwargs):
    #     print(request.session.session_key)
    #     return HttpResponse(content=str(request.session.session_key))
