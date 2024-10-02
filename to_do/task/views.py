# Create your views here.
from django.shortcuts import render, redirect
from .models import Task

# View to display all tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

# View to add a new task
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title') 
        if len(title) >= 2 and len(title) <= 30:
            Task.objects.create(title=title)
            return redirect('task_list')
    return render(request, 'add_task.html')  

# View to mark a task as complete
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

# View to delete a task
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')
