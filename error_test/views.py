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
        """Return the last five published questions."""
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
    #output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('error_test/detail.html')
    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))
    


def result(request):
    #point=0
    #array=[]
    
    #for i in range (2):
    #    ww = request.POST['choice.question.id']
    #    array.append(ww)
    #return HttpResponse(array)
    #if question in request.POST:
    #    q = Question.objects.get(pk=i)
    #    answer_list = q.answer_set.all()
    #    if user==answer_list: 
    #        point = point+1
    #return HttpResponse(point)
    questions = request.POST.getlist('question')
    answers = [request.POST['answer-{}'.format(q)] for q in questions]
    return HttpResponse(answers)
            












class ResultsView(generic.DetailView):
    model = Question
    template_name = 'error_test/results.html'
    
def vote(request, question_id):
    #if 'vote_button' in request.POST:
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        
def addChoice(request,question_id):
    #if 'add_button' in request.POST:
        question = get_object_or_404(Question, pk=question_id)
        choice = request.POST['new_choice']
        if choice != "":
            q = Question.objects.get(pk=question_id)
            q.choice_set.create(choice_text=choice,votes=0)
            return render(request, 'polls/detail.html', {
                'question': question,
 
            })        
        
        

def addQuestionSuccess(request):
    question = request.POST['new_question']
    if question != "":
        q = Question(question_text=question,pub_date=timezone.now())
        q.save()
        return render(request,"polls/addQuestionSuccess.html","")
    else:
        return render(request,"polls/addQuestionFauil.html","")
    
    
