from django.urls import path
from . import views

urlpatterns = [
    # path('api/',views.api)
    path('api/',views.studentView)
]
