from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CreateNewProject, CreateNewTask
from .models import Project, Tasks

# Create your views here.
def hello(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Tasks.objects.filter(project=id)
    return render(request, 'project_detail.html', {
        'project': project, 'tasks': tasks
    })

def delete_task(request, id):
    if request.method == 'GET':
        task = get_object_or_404(Tasks, id=id)
        return render(request, 'delete_task.html', {
            'task': task
        })
    else:
        task = get_object_or_404(Tasks, id=id)
        task.delete()
        return redirect('tasks')



def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Tasks.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=request.POST['project'])
        return redirect('tasks')





