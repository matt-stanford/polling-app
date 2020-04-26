from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('polls', views.polls, name='polls'),
    path('polls/<int:poll_id>', views.poll, name='poll'),
    path('polls/<int:poll_id>/result', views.result, name='result'),
]