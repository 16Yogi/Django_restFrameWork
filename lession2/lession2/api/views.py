from django.shortcuts import render
# from django.http import HttpResponse
from django.http import JsonResponse
from students.models import Student

# def create(request):
#     student = [
#         {'id':1,'name':'mohan'},
#         {'id':2,'name':'kumar'},
#         {'id':3,'name':'suresh'},
#     ]
#     # student = {'id':1,'name':'mohan'}
#     # return HttpResponse("Hello, world! Student")
#     return JsonResponse({'studet':student})


def student_list(request):
    student = Student.objects.all()
    student_list = list(student.values())
    return JsonResponse(student_list,safe=False)