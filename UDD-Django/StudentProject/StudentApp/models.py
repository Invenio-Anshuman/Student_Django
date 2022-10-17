from django.db import models

# Create your models here.
class Student(models.Model):
    ID = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    std = models.CharField(max_length=122)
    sec = models.CharField(max_length=122)
    roll = models.CharField(max_length=122)
