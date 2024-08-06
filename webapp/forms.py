from . import models
from django.forms import ModelForm

class EmailForm(ModelForm):
    class Meta:
        model = models.Email
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Write your name here'
        self.fields['email'].widget.attrs['placeholder'] = 'Write your email here'
        self.fields['message'].widget.attrs['placeholder'] = 'Write your message here'
