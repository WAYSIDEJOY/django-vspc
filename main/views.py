from django.shortcuts import render


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