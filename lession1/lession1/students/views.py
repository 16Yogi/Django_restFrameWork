from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    student = [
        {'rollno':121,'name':'ramu','age':20}
    ]
    return HttpResponse(student)