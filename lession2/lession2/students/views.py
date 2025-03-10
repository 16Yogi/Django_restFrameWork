from django.shortcuts import render
from django.http import HttpResponse

def student(request):
    students = [
        {'id':1,'name':'ramu','age':20}
    ]
    # return HttpResponse("Hello, student!")
    return HttpResponse(students)