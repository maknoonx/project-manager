# projects/forms.py

from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Project, Stage, Task, Company


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'company', 'start_date', 'end_date', 'client']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'client': forms.TextInput(attrs={'class': 'form-control'}),
        }


class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ['number', 'name', 'supervisor', 'recipient', 'start_date', 'end_date']
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'supervisor': forms.TextInput(attrs={'class': 'form-control'}),
            'recipient': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }