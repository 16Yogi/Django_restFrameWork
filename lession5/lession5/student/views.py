from django.shortcuts import render
from django.http import HttpResponse

def student_list(request):
    return HttpResponse("Hello student")