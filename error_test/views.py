import csv
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse
from django.template import loader
from .models import Choice, Question


class IndexView(generic.ListView):
    model = Question
    template_name = 'error_test/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Question
    template_name = 'error_test/detail.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')

def quiz(request):
    question_list = Question.objects.all()
    template = loader.get_template('error_test/detail.html')
    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))
    
def result(request):
    point=0
    i=0
    answers=[]
    question_list = Question.objects.all()
    questions = request.POST.getlist('question')
    for q in questions:
        question = get_object_or_404(Question,pk=q)
        try:
            user_answer = request.POST['user_answer-{}'.format(q)] 
 
        except (KeyError, Choice.DoesNotExist) :
            template = loader.get_template('error_test/detail.html')
            context = {
                'question_list': question_list,
                'error_message': "Please Answer All Questions.",
            }
            return HttpResponse(template.render(context, request))
        else:            
            i=i+1
            if user_answer == 'True': 
                point=point+1
    template = loader.get_template('error_test/result.html')
    context = {
        'question_list': question_list,
        'point': point,
        'total' : i,
    }
    return HttpResponse(template.render(context, request))
    
def howToUse(request):
    template = loader.get_template('error_test/howToUse.html')
    return HttpResponse(template.render(request))

def reference(request):
    template = loader.get_template('error_test/reference.html')
    return HttpResponse(template.render(request))

import csv
from django.http import HttpResponse

def downloadCSVfile(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="error_test.csv"'

    writer = csv.writer(response)
    writer.writerow(['Questions', 'Answer'])
    questions_list = Question.objects.all()
    for q in Question.objects.all():
        for c in q.choice_set.all():
            if c.is_valid:
                writer.writerow([q.question_text,c.choice_text ])

    return response
