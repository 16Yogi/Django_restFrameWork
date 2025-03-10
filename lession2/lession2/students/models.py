from django.db import models

class Student(models.Model):
    roll = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    # class Meta:
    #     db_table = "student"
    #     managed = True

    def __str__(self):
        return self.name