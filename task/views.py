from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import TaskSerializers
from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List': '/task-list/',
        'Detail view': '/task-detail/<str:id>/',
        'Create': '/task-create',
        'Update': '/task-update/<str:id>/',
        'Delete': '/task-delete/<str:id>'
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()   
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request):    

    if request.data["id"]:        
        task = Task.objects.get(id=request.data["id"])
        serializer = TaskSerializers(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    return Response({"message": "missing Id"})

@api_view(['DELETE'])
def taskDelete(request, id):    
    task = Task.objects.get(id=id)
    task.delete()
        
    return Response({"message": "item deleted"})