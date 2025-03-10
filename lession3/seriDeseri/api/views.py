from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import api_view
from rest_framework.decorators import api_view

@api_view(['GET'])
def list_stu(request):
    # students = Student.objects.all()
    # stu_list = list(students.values())
    # return JsonResponse(stu_list,safe=False)
    
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        # return JsonResponse(serializer.data,safe=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
