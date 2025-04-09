# projects/views.py

import json
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.core.serializers.json import DjangoJSONEncoder
from django.db import transaction

from .models import Project, Stage, Task
from .forms import ProjectForm, StageForm, TaskForm

import tempfile
from django.template.loader import render_to_string
from weasyprint import HTML
from django.conf import settings
import os


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'


class ProjectCreateView(SuccessMessageMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('projects:project_list')
    success_message = _("تمت إضافة المشروع بنجاح")
    
    def form_valid(self, form):
        context = self.get_context_data()
        response = super().form_valid(form)
        
        stages_data = self.request.POST.get('stages_data')
        if stages_data:
            stages_list = json.loads(stages_data)
            
            with transaction.atomic():
                for stage_data in stages_list:
                    stage = Stage.objects.create(
                        project=self.object,
                        number=stage_data.get('number'),
                        name=stage_data.get('name'),
                        supervisor=stage_data.get('supervisor'),
                        recipient=stage_data.get('recipient'),
                        start_date=stage_data.get('start_date'),
                        end_date=stage_data.get('end_date')
                    )
                    
                    for task_data in stage_data.get('tasks', []):
                        Task.objects.create(
                            stage=stage,
                            name=task_data.get('name'),
                            description=task_data.get('description', '')
                        )
        
        if self.request.POST.get('save_and_print'):
            return redirect('projects:project_print', pk=self.object.pk)
        
        return response


class ProjectUpdateView(SuccessMessageMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('projects:project_list')
    success_message = _("تم تعديل المشروع بنجاح")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.object:
            stages = []
            for stage in self.object.stages.all():
                tasks = []
                for task in stage.tasks.all():
                    tasks.append({
                        'id': task.id,
                        'name': task.name,
                        'description': task.description
                    })
                
                stages.append({
                    'id': stage.id,
                    'number': stage.number,
                    'name': stage.name,
                    'supervisor': stage.supervisor,
                    'recipient': stage.recipient,
                    'start_date': stage.start_date.strftime('%Y-%m-%d'),
                    'end_date': stage.end_date.strftime('%Y-%m-%d'),
                    'tasks': tasks
                })
            
            context['stages_json'] = json.dumps(stages, cls=DjangoJSONEncoder)
        
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Delete existing stages and tasks
        self.object.stages.all().delete()
        
        # Add new stages and tasks
        stages_data = self.request.POST.get('stages_data')
        if stages_data:
            stages_list = json.loads(stages_data)
            
            with transaction.atomic():
                for stage_data in stages_list:
                    stage = Stage.objects.create(
                        project=self.object,
                        number=stage_data.get('number'),
                        name=stage_data.get('name'),
                        supervisor=stage_data.get('supervisor'),
                        recipient=stage_data.get('recipient'),
                        start_date=stage_data.get('start_date'),
                        end_date=stage_data.get('end_date')
                    )
                    
                    for task_data in stage_data.get('tasks', []):
                        Task.objects.create(
                            stage=stage,
                            name=task_data.get('name'),
                            description=task_data.get('description', '')
                        )
        
        if self.request.POST.get('save_and_print'):
            return redirect('projects:project_print', pk=self.object.pk)
        
        return response


class ProjectDeleteView(SuccessMessageMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('projects:project_list')
    success_message = _("تم حذف المشروع بنجاح")


def project_print_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    # Just render the print-friendly HTML template
    return render(request, 'projects/project_print.html', {
        'project': project,
        'print_mode': True
    })