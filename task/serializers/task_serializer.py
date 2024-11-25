from rest_framework import serializers
from task.models.task import Task
from django.utils.translation import gettext_lazy as _


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
                    'id',
                    'title',
                    'description',
                    'created_at',
                    'completed',
                ]
    