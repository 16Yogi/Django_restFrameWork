from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # web app endpoint
    path('student/',include('students.urls')),
    
    # api endpoint
    path('api/v1/',include('api.urls')),
]
