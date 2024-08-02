from django.shortcuts import render
from .models import Project, Job
from .forms import EmailForm

# Create your views here.
def index(request):
    jobs = Job.objects.all()
    return render(request, 'index.html', {'jobs': jobs})


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    form = EmailForm()
    return render(request, 'contact.html', {'form': form})
