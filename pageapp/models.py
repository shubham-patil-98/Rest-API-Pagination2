from operator import mod
from django.db import models
from django.forms import IntegerField

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    roll=models.IntegerField()
    std=models.IntegerField()