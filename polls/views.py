from django.shortcuts import render
from .models import Question, Choice

def index(request):
    return render(request, 'pages/index.html', {})

def polls(request):
    polls = Question.objects.all
    return render(request, 'pages/polls.html', {'polls': polls})


def poll(request, poll_id):
    poll = Question.objects.filter(pk=poll_id)
    choices = Choice.objects.all
    context = {
        'poll': poll,
        'choices': choices
    }
    return render(request, 'pages/poll.html', context)
