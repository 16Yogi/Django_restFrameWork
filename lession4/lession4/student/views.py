from django.shortcuts import render
from django.http import HttpResponse

def stu(request):
    return HttpResponse("Welcome to Student Page")