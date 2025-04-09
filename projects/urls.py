from django.urls import path
from . import views

app_name = 'projects'  # Namespace for the app

urlpatterns = [
    # Main project listing page (home page)
    path('', views.ProjectListView.as_view(), name='project_list'),
    
    # Add new project
    path('add/', views.ProjectCreateView.as_view(), name='project_add'),
    
    # Edit existing project
    path('<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project_edit'),
    
    # Delete project
    path('<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    
    # Print project details (PDF generation)
    path('<int:pk>/print/', views.project_print_view, name='project_print'),
]