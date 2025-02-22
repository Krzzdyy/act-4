from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=20)  
    name = models.CharField(max_length=100)
    year_section = models.CharField(max_length=20) 

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.year_section}"
