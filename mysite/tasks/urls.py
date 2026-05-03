from . import views, admin
from django.urls import path

urlpatterns = [
    path('', views.show_tasks, name='tasks'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('status/<int:task_id>', views.task_status, name='task_status'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('signup/', views.signup, name='signup'),
]

