from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name