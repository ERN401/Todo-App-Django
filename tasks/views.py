from django.shortcuts import get_object_or_404, render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()

    context = {
        'tasks': tasks
    }

    return render(request, 'list.html', context)

def add(request):
    title = request.POST['title']  

    if title == '':
        return redirect('index')
    else:
        task = Task(title=title)
        task.save()
        return redirect('index')
    return render(request, 'list.html')

def delete(request):
    id = request.POST['id']

    task = Task.objects.filter(pk=id)

    task.delete()
    
    return redirect('index')

def deleteAll(request):
    task = Task.objects.all()
    task.delete()
    return redirect('index')

def update_page(request, task_id): 
    task = Task.objects.get(id=task_id)

    context = {
        'task': task
    }

    return render(request, 'update_page.html', context)

def update(request, task_id):
    new_task = Task.objects.filter(pk=task_id)

    title = request.POST['title']
    completed = request.POST.get('check', False)

    if completed == 'on':
        new_task.update(title=title, completed=True)
    else:
        new_task.update(title=title, completed=False)

    # print(title)
    # completed = request.POST['completed']
    # task = Task(title=title)

    # new_task.save()

    return redirect('index')



