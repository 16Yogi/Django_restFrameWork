from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include('students.urls')),
    path('api/v1/',include('api.urls')),
]
