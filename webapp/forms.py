from . import models
from django.forms import ModelForm

class EmailForm(ModelForm):
    class Meta:
        model = models.Email
        fields = ['name', 'email', 'message']

