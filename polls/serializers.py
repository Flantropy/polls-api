from rest_framework import serializers
from .models import Poll, Question


class PollSerializer(serializers.HyperlinkedModelSerializer):
    questions = serializers.HyperlinkedRelatedField(many=True,
                                                    view_name='question-detail',
                                                    read_only=True)

    class Meta:
        fields = ['name', 'description', 'url', 'questions']
        model = Poll


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['question_text', 'poll']
        model = Question
