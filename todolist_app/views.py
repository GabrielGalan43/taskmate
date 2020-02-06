# ! python3
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator # This class is used in pagination.
from django.http import HttpResponse # -- Make some research about HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm


# Create your views here.
def index(request):
    context = {
        "index_text":"Welcome to Taskmate!."
        }
    
    return render(request, 'index.html', context )


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        # This method requires two parameters "request" and the "message".
        messages.success(request, ("New Task Added!"))
        return redirect('todolist')
    else: # Everything from this line down is executed if we issue a "GET" request.
        all_tasks = TaskList.objects.all()
        # This instance requires 2 parameters. The number passed is the number
        # of items that are going to be displayed in the page.
        paginator = Paginator(all_tasks, 10) 
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)

        return render(request, 'todolist.html', {'all_tasks': all_tasks})


def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id) # 'pk' means 'primary key'.
    task.delete()
    return redirect('todolist')


def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id) # 'pk' means 'primary key'.
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()

        messages.success(request, ("Task Edited!"))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})
  

def complete_task(request, task_id):
   task = TaskList.objects.get(pk=task_id) # 'pk' means 'primary key'.
   task.done = True  # Here we change the defaul "False" value to "True".
   task.save()
   return redirect('todolist')

def pending_task(request, task_id):
   task = TaskList.objects.get(pk=task_id) # 'pk' means 'primary key'.
   task.done = False  # Here we change the defaul "False" value to "True".
   task.save()
   return redirect('todolist')

  
def contact(request):
    context = {
        "contact_text":"Welcome to Contact App."
        }
    return render(request, 'contact.html', context)


def about(request):
    context = {
        "about_text":"Welcome to About App."
        }
    return render(request, 'about.html', context)