from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    link = models.URLField(max_length=200)
    image = models.FileField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=30)
    company = models.CharField(max_length=30, default='COMPANY')
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    logo = models.FileField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Email(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()

