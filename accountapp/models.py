from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.CharField(max_length=11, unique=True, primary_key=True)
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE)

class Grade(models.Model):
    grade = models.IntegerField(default='1')
    point = models.IntegerField(null=True)
