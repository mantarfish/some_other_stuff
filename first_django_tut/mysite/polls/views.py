from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from .forms import QuestionForm
from django.views import generic
from django.utils import timezone


'''

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})

def detail(request, pk):
    ''''url funtion captures question_id and send it as argument to view funtion''''

    question = Question.objects.get(pk=pk)
    return render(request,'polls/detail.html' ,{'question': question})

def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    # question = Question.objects.get(pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
'''
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
    

class ResultView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
    


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'you did not make a choice'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=[question.id]))

def createchoice(request, question_id):
    
    if request.POST:
        choice_text = request.POST['choice_text']
        question = Question.objects.get(pk=question_id)
        Choice.objects.create(
            choice_text = choice_text,
            question = question,
            votes = int(0)
        )
        return HttpResponseRedirect(reverse('polls:detail', args=[question_id]))
    else:
    
        return render(request, 'polls/createchoice.html', {'question_id':question_id})
        # return HttpResponse('hello')

def home(request):
    return render(request, 'polls/home.html')
