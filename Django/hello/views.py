from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request): #server returns hello world on response
    return render(request, "hello/index.html") #returns html template
    #best practice to include hello in folder

def thomas(request):
    return HttpResponse('fart')


def fartgobler(request):
    return HttpResponse('oemgee')


def greet(request,name): #dynamically renders based off param
    return render(request,"hello/greet.html", {
        "name": name.capitalize()
    }) #3rd argument called context
    #info provided to template (variables)