from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название задачи',
                'aria-label': 'Task-title'
            }),
        }

    def clean_title(self):
        title = self.cleaned_data['title']


        if title:
            title = title.strip()


        if len(title) < 3:
            raise forms.ValidationError("Task title must be at least 3 characters long")

        elif len(title) > 200:
            raise forms.ValidationError("Task title must not be longer than 200 characters")

        return title


class ExtendedUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Создаем поля родителя
        for field in self.fields.values():  # "Красим" все поля сразу
            field.widget.attrs['class'] = 'form-control'


class ExtendedAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'