from django.shortcuts import render, redirect

import tasks
from tasks.models import Task


# Create your views here.

def show_tasks(request):
    if request.method == 'POST':
        title_form = request.POST.get('title')
        title_form = title_form.strip()

        if title_form and not Task.objects.filter(title=title_form).exists():
            Task.objects.create(title=title_form)
            return redirect('tasks')


    tasks = Task.objects.order_by('status', '-created_date')
    return render(request, 'tasks/todo_list.html', {'tasks': tasks})


def delete_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(pk=task_id)
        task.delete()

    return redirect('tasks')

def task_status(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(pk=task_id)
        task.status = not task.status
        task.save()
    return redirect('tasks')

def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        new_title = request.POST.get('title')
        task.title = new_title
        task.save()
        return redirect('tasks')


    return render(request, 'tasks/edit_task.html', {'task': task})