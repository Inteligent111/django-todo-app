from . import views, admin
from django.urls import path

urlpatterns = [
    path('', views.show_tasks, name='tasks'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]