from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from task.models.task import Task
from task.serializers.task_serializer import TaskSerializer


class TaskAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class= [TaskSerializer]

    def get(self, request):   

        tasks= Task.objects.filter(user= request.user)

        data= TaskSerializer(tasks, many=True).data


        return Response(data=data, status=status.HTTP_200_OK)
    
    def post(self, request):   

        serializer= TaskSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user']= request.user
        serializer.save()


        return Response(status=status.HTTP_201_CREATED)
    


    def put(self, request):   

        try:
            task_id= request.data['task_id']
            task= Task.objects.get(id= task_id)
        except KeyError:
            return Response(data={"message": 'task_id is requierd'}, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response(data={"message": 'task does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        serializer= TaskSerializer(task, data= request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response(status=status.HTTP_201_CREATED)
    