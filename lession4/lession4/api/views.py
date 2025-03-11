from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


def api(request):
    return HttpResponse("Hello, api!")

def stu_list(request):
    student = Student.objects.all()
    student_list = list(student.values())
    return JsonResponse(student_list, safe=False)
@api_view(['GET','POST'])
def studentOpr(request):
    if request.method == 'GET':
        stu = Student.objects.all()
        serializers = StudentSerializer(stu,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        else:
            print(serializers.errors)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def studentDetailsView(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    