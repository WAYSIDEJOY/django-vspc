from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    return render(request, 'main/index.html')


def blog(request):
    return render(request, 'main/blog.html')


def candidate(request):
    return render(request, 'main/candidate.html')


def contact(request):
    return render(request, 'main/contact.html')


def elements(request):
    return render(request, 'main/elements.html')


def job_details(request):
    return render(request, 'main/job_details.html')


def jobs(request):
    return render(request, 'main/jobs.html')


def singleblog(request):
    return render(request, 'main/singleblog.html')


def tasks(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/Tasks.html', {'title': 'Таблица', 'tasks' : tasks} )


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tasks')
        else:
            error = 'ошибка'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)