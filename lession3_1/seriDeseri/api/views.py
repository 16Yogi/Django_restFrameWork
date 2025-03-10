from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from student.models import Student

def api(request):
    # return HttpResponse("Hello, api")
    students = Student.objects.all()
    stundent_list = list(students.values())
    return JsonResponse(stundent_list, safe=False)
    
    