from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
#import from the file models in current dir .
from .models import Question
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("this is the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question {}s.".format(question_id))

def results(request, question_id):
    response = "You're looking at the results of the question {}s."
    return HttpResponse(response.format(question_id))

def vote(request, question_id):
    return HttpResponse("You're voting on question {}s.".format(question_id))

def index(request):
    #calls the django template
    queued_question = Question.objects.order_by("-pub_date")[:5]#?
    template = loader.get_template("polls/index.html")
    context = {"queued_question": queued_question}
    return HttpResponse(template.render(context, request))

'''another way to render in django using render()

def index(request):
    queued_question = Question.objects.order_by("-pub_date")[;5]
    context = {"queued_question": queued_question}
    return render(request, "polls/index.html", context)
'''

#def detail(request, question_id):
 #   question = get_object_or_404(Question, pk=question_id)
  #  return render(request, "polls/index.html", {"question":question})
