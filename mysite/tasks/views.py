from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from tasks.models import Task
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import TaskForm



# Create your views here.
@login_required  # Теперь страница доступна только после входа
def show_tasks(request):
    form = TaskForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("tasks")
    tasks = Task.objects.filter(user=request.user).order_by('status', '-created_date')
    return render(request, 'tasks/todo_list.html', {'form': form, 'tasks': tasks})



@login_required
@require_POST
def delete_task(request, task_id):

    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()

    return redirect('tasks')


@login_required
@require_POST
def task_status(request, task_id):
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        task.status = not task.status
        task.save()
        return redirect('tasks')


@login_required
def edit_task(request, task_id):
    tasks = get_object_or_404(Task, pk=task_id, user=request.user)
    form = TaskForm(request.POST or None, instance=tasks)
    if request.method == "POST":
        if form.is_valid():

            form.save()

            return redirect('tasks')

    return render(request, 'tasks/edit_task.html', {'tasks': tasks, 'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Сразу логиним пользователя после регистрации
            return redirect('tasks')  # Имя твоего пути со списком задач
    else:
        # Если это GET запрос, создаем пустую форму
        form = UserCreationForm()

    # Это выполняется, если форма невалидна ИЛИ если это GET запрос
    return render(request, 'registration/signup.html', {'form': form})



