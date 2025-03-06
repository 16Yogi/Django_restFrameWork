from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from students.models import Student

def studentView(request):
    # students = {
    #     'id':1,
    #     'name':'mohan',
    #     'class':'CS'
    # }
    students = Student.objects.all()
    # print(students)
    students_list = list(students.values())
    return JsonResponse(students_list,safe=False)