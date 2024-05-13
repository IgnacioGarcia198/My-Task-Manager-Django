from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Task
from .forms import TaskForm
from django.http import HttpResponseRedirect

def index(request):
    return redirect('task_manager:all_tasks')

def all_tasks(request):
    task_list = Task.objects.order_by("due_date")
    context = { "task_list": task_list } if task_list.exists() else {}
    return render(request, "TaskManagerApp/all_tasks.html", context)

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_manager:all_tasks')
    else:
        form = TaskForm()

    return render(request, 'TaskManagerApp/create_task.html', {'form': form})

def task_detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, "TaskManagerApp/task_detail.html", {"task": task})

def toggle_task_done(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.is_done = not task.is_done
    task.save()
    referer_url = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(referer_url)

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('task_manager:all_tasks')