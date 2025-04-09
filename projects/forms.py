# projects/forms.py

from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Project, Stage, Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'company', 'company_logo', 'start_date', 'end_date', 'client']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ['number', 'name', 'supervisor', 'recipient', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description']