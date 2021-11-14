from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Question, Polls, Choice, Vote
from django.template import loader


def index(request):
    latest_Polls_list = Polls.objects.order_by('-s_date')
    template = loader.get_template('polls/index.html')
    context = {
        'latest_Polls_list': latest_Polls_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, poll_id):
    latest_Polls_list = Polls.objects.filter(pk=poll_id)
    template = loader.get_template('polls/detail.html')
    context = {
        'latest_Polls_list': latest_Polls_list,
    }
    return HttpResponse(template.render(context, request))


def detail_of_details(request, poll_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail_of_details.html', {'question': question})


def vote(request, question_id):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    question = get_object_or_404(Question, pk=question_id)
    choice = get_object_or_404(Choice, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        if Vote.objects.filter(voter=ip, choice=choice):
            return render(request, 'polls/detail_of_details.html', {
                'question': question,
                'error_message': "You are already voted.",
            })
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail_of_details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        Vote.objects.create(voter=ip, choice=choice)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
