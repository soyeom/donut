from django.contrib.auth.models import AbstractUser
from django.db import models

class User(models.Model):
    userid = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    birth_day = models.CharField(max_length=150)
