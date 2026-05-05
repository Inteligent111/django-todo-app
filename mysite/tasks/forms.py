from django import forms
from .models import Task



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']


    def clean_title(self):
        title = self.cleaned_data['title']


        if title:
            title = title.strip()


        if len(title) < 3:
            raise forms.ValidationError("Task title must be at least 3 characters long")

        elif len(title) > 200:
            raise forms.ValidationError("Task title must not be longer than 200 characters")

        return title