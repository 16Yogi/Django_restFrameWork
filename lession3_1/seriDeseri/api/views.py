from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# def api(request):
    # return HttpResponse("Hello, api")
    # students = Student.objects.all()
    # stundent_list = list(students.values())
    # return JsonResponse(stundent_list, safe=False)
@api_view(['GET','POST'])
def studentView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serilizer = StudentSerializer(students,many=True)
        return Response(serilizer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serilizer = StudentSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        else:
            print(serilizer.errors)
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
        