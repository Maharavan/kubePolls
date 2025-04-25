import json
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from members.models import VoteQuestions
from members.models import Choices
from django.shortcuts import redirect
from django.urls import reverse

def members(request):
    template = loader.get_template('index.html') 
    return HttpResponse(template.render())

def ask_question(request):
    template = loader.get_template('askPolls.html')
    return HttpResponse(template.render())  

@csrf_exempt
def poll_list(request):
    if request.method == 'POST':
        question_text = request.POST.get('name_field')
        choice_list = [request.POST.get(f'choice{i}') for i in range(1, 6) if request.POST.get(f'choice{i}')]
        
        if question_text:
            question = VoteQuestions.objects.create(question=question_text)
            for choice in choice_list:
                if choice.strip():
                    Choices.objects.create(question_id=question, choice=choice.strip())

        return redirect('poll-list')

    data = VoteQuestions.objects.all()
    print(data)
    print(Choices.objects.all())
    template = loader.get_template('viewPolls.html')
    context = {'questions': data}
    return HttpResponse(template.render(context, request))

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.urls import reverse
from .models import Choices
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def live_polls(request):
    if request.method == 'GET':
        question_id = request.GET.get('id')
        question_text = request.GET.get('text')
        choices = Choices.objects.filter(question_id=question_id)
        
        template = loader.get_template('livePolls.html')
        context = {
            'question_text': question_text,
            'choices': choices
        }
        return HttpResponse(template.render(context, request))

    elif request.method == 'POST':
        try:
            choice_id = request.POST.get('select_choice')
            selected_choice = Choices.objects.get(id=choice_id)
            selected_choice.vote += 1
            selected_choice.save()

            return HttpResponseRedirect(reverse('poll_results') + f'?question_id={selected_choice.question_id.id}')
        except Choices.DoesNotExist:
            raise Http404('Choice doesnt exist')

    else:
        return HttpResponseBadRequest("Unsupported HTTP method.")

def poll_results(request):
    question_id = request.GET.get('question_id')
    
    if not question_id:
        return HttpResponseBadRequest("No question ID provided.")
    
    try:
        question = Choices.objects.get(id=question_id).question_id
    except Choices.DoesNotExist:
        return HttpResponseBadRequest("Invalid question ID.")
    
    choices = Choices.objects.filter(question_id=question_id)
    total_votes = sum(ch.vote for ch in choices)
    
    for ch in choices:
        ch.percent = round((ch.vote / total_votes) * 100, 2) if total_votes > 0 else 0
    
    template = loader.get_template('pollResults.html')
    context = {
        'question_text': question.question,
        'choices': choices
    }
    return HttpResponse(template.render(context, request))

