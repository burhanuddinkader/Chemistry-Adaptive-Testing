from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from mole.models import Question
# Create your views here.
def index(request):
    context={}
    quest=Question.objects.all()
    context={quest:"quest"}
    return render(request,"questions.html",context)
