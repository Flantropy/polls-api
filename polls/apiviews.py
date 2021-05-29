from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Poll, Question
from .serializers import PollSerializer, QuestionSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionList(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.filter(poll_id=self.kwargs['pk'])
        return queryset

    def perform_create(self, serializer):
        # serializer.data['poll_id'] = self.kwargs['pk']
        serializer.save(poll=Poll.objects.get(pk=self.kwargs['pk']))


# class CreateVote(APIView):
#     serializer_class = VoteSerializer
#
#     def post(self, request, pk, choice_pk):
#         voted_by = request.data.get('voted_by')
#         data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
#         serializer = VoteSerializer(data=data)
#         if serializer.is_valid():
#             vote = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
