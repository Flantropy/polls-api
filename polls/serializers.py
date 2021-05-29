from rest_framework import serializers
from .models import Poll, Question


class QuestionSerializer(serializers.ModelSerializer):
    # votes = VoteSerializer(many=True, required=False)
    class Meta:
        model = Question
        fields = [
            'poll',
            'question_text',
            'expected_answer_type',
            'answer_variant_1',
            'answer_variant_2',
            'answer_variant_3',
            'answer_variant_4'
        ]


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'
