from .models import article
from django.forms import ModelForm, TextInput, Textarea, FileInput

class articleForm(ModelForm):
    class Meta:
        model = article
        fields = ['topic', 'author', 'description', 'photo']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
            }),
            'photo': FileInput(attrs={
                'class': 'custom-file-upload',
                'id': "image-input"
                #'onchange': 'showImage(this);'
            })
        }