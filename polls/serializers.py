from rest_framework import serializers
from .models import Poll, Question, Answer, Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Vote
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Question
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'
