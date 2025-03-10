from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(max_length=30)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.name
