from .models import Task
from django.forms import ModelForm, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите задачу"
            }),
            "task": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите описание"
            })
        }
