from django.shortcuts import render
from .models import Student
from . serializers import StudentSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def Details(request):
    if request.method =='GET':
       student=Student.objects.all()
       serializer=StudentSerializer(student,many=True)
       return JsonResponse(serializer.data,safe=False)
    
    if request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def Details_list(request,id):
    try:
        student=Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)

