from django.http import JsonResponse
from django.http import HttpResponse
from student.models import Student

def student_list(request):
    students = Student.objects.all()
    stu = list(students.values())
    return JsonResponse(stu,safe=False)