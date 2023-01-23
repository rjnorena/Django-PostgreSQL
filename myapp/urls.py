from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name='index'),
    path("about/", views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('project_detail/<int:id>', views.project_detail, name='project_detail'),
    path('tasks/', views.tasks, name='tasks'),
    path('delete_task/<int:id>', views.delete_task, name='delete_task'),
    path('create_project/', views.create_project, name='create_project'),
    path('create_task/', views.create_task, name='create_task')
    ]