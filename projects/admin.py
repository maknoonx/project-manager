# projects/admin.py

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Company, Project, Stage, Task


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1


class StageInline(admin.TabularInline):
    model = Stage
    extra = 1
    show_change_link = True


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_preview')
    search_fields = ('name',)
    
    def logo_preview(self, obj):
        if obj.logo:
            return f'<img src="{obj.logo.url}" width="50" height="50" />'
        return '(No logo)'
    
    logo_preview.short_description = _('Logo Preview')
    logo_preview.allow_tags = True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'start_date', 'end_date', 'client', 'get_stages_count')
    list_filter = ('start_date', 'end_date', 'company')
    search_fields = ('name', 'company__name', 'client')
    raw_id_fields = ('company',)
    inlines = [StageInline]
    
    def get_stages_count(self, obj):
        return obj.stages.count()
    
    get_stages_count.short_description = _('عدد المراحل')


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ('project', 'number', 'name', 'supervisor', 'recipient', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date', 'project')
    search_fields = ('name', 'supervisor', 'recipient')
    inlines = [TaskInline]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'stage', 'get_project')
    list_filter = ('stage__project',)
    search_fields = ('name', 'description')
    
    def get_project(self, obj):
        return obj.stage.project
    
    get_project.short_description = _('المشروع')
    get_project.admin_order_field = 'stage__project'