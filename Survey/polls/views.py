import json
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Question, Choice, Polls
from .serializers import QuestionSerializer, ChoiceSerializer, VoteSerializer, QuestionResultPageSerializer, \
    PollSerializer


@csrf_exempt
def questions_view(request):
    if request.method == 'GET':
        return HttpResponse("Not Implemented")


@api_view(['GET'])
def questions_view(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PATCH', 'DELETE'])
def question_detail_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionSerializer(question).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        question.delete()
        return Response("Question deleted", status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def choices_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    serializer = ChoiceSerializer(data=request.data)
    if serializer.is_valid():
        choice = serializer.save(question=question)
        return Response(ChoiceSerializer(choice).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def vote_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    serializer = VoteSerializer(data=request.data)
    if serializer.is_valid():
        choice = get_object_or_404(Choice, pk=serializer.validated_data['choice_id'], question=question)
        choice.votes += 1
        choice.save()
        return Response("Voted")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def question_result_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    serializer = QuestionResultPageSerializer(question)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def polls_view(request):
    if request.method == 'GET':
        polls = Polls.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PollSerializer(data=request.data)
        if serializer.is_valid():
            title_p = request.data['title_p']
            desc_p = request.data['desc_p']
            start_date = datetime.strptime(request.data['s_date'], '%Y-%m-%d')
            end_date = datetime.strptime(request.data['e_date'], '%Y-%m-%d')
            Polls.objects.create(title_p=title_p, desc_p=desc_p, s_date=start_date, e_date=end_date)
            return HttpResponse("poll created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def polls_detail_view(request, poll_id):
    poll = get_object_or_404(Polls, pk=poll_id)
    if request.method == 'GET':
        serializer = PollSerializer(poll)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = PollSerializer(poll, data=request.data, partial=True)
        if serializer.is_valid():
            poll = serializer.save()
            return Response(PollSerializer(poll).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        poll.delete()
        return Response("Question deleted", status=status.HTTP_204_NO_CONTENT)
