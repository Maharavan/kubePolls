from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='home'), 
    path('create-polls/', views.ask_question, name='ask-question'),
    path('poll-list/', views.poll_list, name='poll-list'),
    path('live-polls/', views.live_polls, name='live-polls'),
    path('poll-results/', views.poll_results, name='poll_results')]