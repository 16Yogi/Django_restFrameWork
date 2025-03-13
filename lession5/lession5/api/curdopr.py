from django.http import HttpResponse
from django.http import JsonResponse
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET','POST'])
def student(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializers = StudentSerializer(students,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        else:
            print(serializers.errors)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # elif request.method == 'PUT':
    #     serializers = StudentSerializer(student,data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data,status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','POST'])
def student_put(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)