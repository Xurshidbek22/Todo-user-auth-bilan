from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    fullname = models.CharField(max_length=50)
    guruh = models.CharField(max_length=50)
    st_raqam = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):return self.fullname

class Todo(models.Model):
    nom = models.CharField(max_length=50)
    vaqt = models.DateField()
    tarixi = models.CharField(max_length=255)
    stats = models.CharField(max_length=50)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nom