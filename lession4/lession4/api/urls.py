from django.urls import path
from . import views

urlpatterns = [
    path('api/',views.api),
    path('stu_list_api/',views.stu_list),
    # path('studentOpr/',views.studentOpr),
    path('student/<int:pk>/',views.studentDetailsView)
]
