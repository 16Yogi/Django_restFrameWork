from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def api_view(request):
    return HttpResponse('Hello api!')