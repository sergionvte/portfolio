from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    link = models.URLField(max_length=200)
    image = models.FileField(upload_to='project_images/')

    def __str__(self):
        return self.title
