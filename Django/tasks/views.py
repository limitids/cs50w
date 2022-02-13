from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task") #creates form with charfield input
    ##priority = forms.IntegerField(label="Priority",min_value=1,max_value=5)


def index(request):
    if "tasks" not in request.session: #looks in session to find tasks
        request.session["tasks"] = []
    return render(request, 'tasks/index.html', {
        "tasks": request.session['tasks']
    })

def add(request):
    if request.method == "POST":
       form = NewTaskForm(request.POST) #server validation
       if form.is_valid(): #checks validity of data with server
           task = form.cleaned_data["task"]
           request.session["tasks"] += task #if form is valid apends to list
           return HttpResponseRedirect(reverse('tasks:index'))
       else: #if not valid
            return render(request,"tasks:index", {
                "form": form #returns form
            })

    return render(request,'tasks/add.html', {
        "form": NewTaskForm()
    })