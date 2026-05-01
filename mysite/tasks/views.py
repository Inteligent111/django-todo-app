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


    tasks = Task.objects.all()
    return render(request, 'tasks/todo_list.html', {'tasks': tasks})


def delete_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(pk=task_id)
        task.delete()

    return redirect('tasks')

