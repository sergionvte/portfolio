from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    return render(request, 'index.html')


def work(request):
    projects = Project.objects.all()
    for project in projects:
        print(project.image)
    return render(request, 'work.html', {'projects': projects})


def contact(request):
    return render(request, 'contact.html')
