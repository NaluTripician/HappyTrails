from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader


def index(request, question_id):
    context = {
        'question_id': question_id,
    }
    return render(request, 'HappyTrailsApp/index.html', context)

def nalu(request, question_id):
    return HttpResponse("Nalu Sucks %s Butts." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)