from django.shortcuts import render
from .models import Question, Choice

def index(request):
    return render(request, 'pages/index.html', {})

def polls(request):
    polls = Question.objects.order_by('-pub_date')
    return render(request, 'pages/polls.html', {'polls': polls})


def poll(request, poll_id):
    poll = Question.objects.get(pk=poll_id)
    return render(request, 'pages/poll.html', {'poll': poll})

def result(request, poll_id):
    poll = Question.objects.get(pk=poll_id)
    return render(request, 'pages/result.html', {'poll': poll})
