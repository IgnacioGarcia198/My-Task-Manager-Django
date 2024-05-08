from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Task

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def all_tasks(request):
    task_list = Task.objects.order_by("due_date")
    context = { "task_list": task_list } if task_list.exists() else {}
    return render(request, "TaskManagerApp/all_tasks.html", context)

def task_detail(request, task_id):
    #return HttpResponse("You're looking at task %s." % task_id)
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, "TaskManagerApp/task_detail.html", {"task": task})