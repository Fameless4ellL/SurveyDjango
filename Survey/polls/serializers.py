from rest_framework import serializers
from .models import Question, Choice, Polls


# class QASerializer(serializers.ModelSerializer):
#     QA = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), many=True)
#
#     class Meta:
#         model = Polls
#         fields = ('id', 'descriptionQA', 'typeQA')

class PollSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title_p = serializers.CharField(max_length=56)
    desc_p = serializers.CharField(max_length=255)
    s_date = serializers.DateTimeField(read_only=True)
    e_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Polls.objects.create(**validated_data)


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    descriptionQA = serializers.CharField(max_length=255)
    typeQA = serializers.CharField(max_length=55)

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class ChoiceSerializer(serializers.Serializer):
    choice_text = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Choice.objects.create(**validated_data)


class QuestionDetailPageSerializer(QuestionSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)


class VoteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()


class ChoiceSerializerWithVotes(ChoiceSerializer):
    votes = serializers.IntegerField(read_only=True)


class QuestionResultPageSerializer(QuestionSerializer):
    choices = ChoiceSerializerWithVotes(many=True, read_only=True)
