from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from task.models.task import Task
from task.serializers.task_serializer import TaskSerializer


class TaskAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):   

        tasks= Task.objects.filter(user= request.user)

        data= TaskSerializer(tasks, many=True).data


        return Response(data=data, status=status.HTTP_200_OK)
    