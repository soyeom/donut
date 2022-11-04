from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.CharField(max_length=11, unique=True, primary_key=True)
    username = models.CharField(max_length=30, unique=False)
    USERNAME_FIELD = 'email'
    grade = models.ForeignKey('Grade', models.SET_NULL, blank=True, null=True)

class Grade(models.Model):
    grade = models.IntegerField(default='1')
    point = models.IntegerField(null=True)
