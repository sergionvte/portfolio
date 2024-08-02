import sendgrid
import json
from sendgrid.helpers.mail import Mail, Email, To
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Project
from .forms import EmailForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


def work(request):
    projects = Project.objects.all()
    return render(request, 'work.html', {'projects': projects})

def contact(request):
    form = EmailForm()
    return render(request, 'contact.html', {'form': form})
