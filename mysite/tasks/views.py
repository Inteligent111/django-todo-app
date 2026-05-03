from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from tasks.models import Task
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required  # Теперь страница доступна только после входа
def show_tasks(request):
    if request.method == 'POST':
        title_form = request.POST.get('title')
        title_form = title_form.strip()

        # Проверяем уникальность задачи ТОЛЬКО для текущего пользователя
        if title_form and not Task.objects.filter(title=title_form, user=request.user).exists():
            Task.objects.create(title=title_form, user=request.user) # Привязываем автора
            return redirect('tasks')

    # Забираем только задачи того, кто вошел на сайт
    tasks = Task.objects.filter(user=request.user).order_by('status', '-created_date')
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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Сразу логиним пользователя после регистрации
            return redirect('todo_list')  # Имя твоего пути со списком задач
    else:
        # Если это GET запрос, создаем пустую форму
        form = UserCreationForm()

    # Это выполняется, если форма невалидна ИЛИ если это GET запрос
    return render(request, 'registration/signup.html', {'form': form})