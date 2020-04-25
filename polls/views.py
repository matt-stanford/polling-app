from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html', {})

def polls(request):
    return render(request, 'pages/polls.html', {})
