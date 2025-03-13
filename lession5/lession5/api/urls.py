from django.urls import path
from . import views
from . import student_list
from . import curdopr

urlpatterns = [
    path('api/',views.api_view),
    path('stu_list/',student_list.student_list),
    path('curd/',curdopr.student),
    path('curdopr/<int:pk>',curdopr.student_put),
]
