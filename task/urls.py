
from task.views.task_view import TaskAPIView
from django.urls import path

urlpatterns = [
    path('', TaskAPIView.as_view(), name='task'),
   
]
