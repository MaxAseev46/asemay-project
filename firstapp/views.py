from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello World! Это мой первый проект на Django!")

def about(request):
    return HttpResponse("<h2>0 сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Koнтaкты</h2>")