from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
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


def vote(request, poll_id):
    poll = get_object_or_404(Question, pk=poll_id)
    try:
        choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError):
        return render(request, 'pages/poll.html', {'poll': poll})
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('result', args=(poll.id,)))

