from django.shortcuts import render, redirect
from django.core.mail import send_mail
from portfolio.settings import EMAIL_HOST_USER
from .utils.functions import check_mail
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
    form = EmailForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        subject = 'Message from portfolio'
        content = f'Name: {name}\nEmail: {email}\nMessage: {message}'

        if check_mail(email):
            send_mail(
                subject,
                content,
                EMAIL_HOST_USER,
                [EMAIL_HOST_USER],
            )
            return redirect('success')
        else:
            form.add_error(None, 'This email account does not exist.')
    else:
        form = EmailForm()

    return render(request, 'contact.html', {'form': form})


def success(request):
    return render(request, 'success.html')
