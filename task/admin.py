from django.contrib import admin
from task.models.task import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    # pass
    model = Task
    list_display = ['user',
                    'title',
                    'description',]


admin.site.register(Task, TaskAdmin)