from django.shortcuts import render, redirect
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from .models import Task
from django.utils import timezone
from tasks.tasks import send_task_reminder

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            if request.user:
                task.user = request.user
                task.save()
                return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/tasks_form.html', {'form': form})

@login_required
def task_list(request):
    return render(request, 'tasks/tasks_list.html', {'tasks': Task.objects.filter(user=request.user)})

@login_required
def task_list_incomplete(request):
    return render(request, 'tasks/tasks_list.html', {'tasks': Task.objects.filter(user=request.user, completed=False)})

@login_required
def task_list_complete(request):
    return render(request, 'tasks/tasks_list.html', {'tasks': Task.objects.filter(user=request.user, completed=True)})

@login_required
def task_list_overdue(request):
    return render(request, 'tasks/tasks_list.html', {'tasks': Task.objects.filter(user=request.user, completed=False, due_date__lte=timezone.now())})

@login_required
def delete_task(request, task_id):
    try:
        task = Task.objects.get(uuid=task_id)
        if request.user == task.user:
            task.delete()
            print(f'{task_id} deleted successfully')
        else:
            print(f'User {request.user} is not authorised to delete task assigned to {task.user} - id: {task_id}')
        return redirect('task_list')
    except Exception as e:
        print(f"Requested task not able to be deleted - id {task_id} - {e}")


@login_required
def toggle_task_completion(request, task_id):
    try:
        task = Task.objects.get(uuid=task_id)
        if request.user == task.user:
            if task.completed:
                task.completed = False
            else:
                task.completed = True
            task.save(update_fields=["completed"])
            return redirect('task_list')
        else:
            print(f'User {request.user} is not authorised to delete task assigned to {task.user} - id: {task_id}')
    except Exception as e:
        print(f"Requested task not able to be modified - id {task_id} - {e}")


def send_task_reminder(task):
    send_task_reminder.delay(task.uuid)