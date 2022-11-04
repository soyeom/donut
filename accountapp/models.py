from django.db import models


class User(models.Model):
    id = models.CharField(max_length=11, unique=True, primary_key=True)
    password = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    email = models.EmailField(max_length=100, unique=True)
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE,null=True)


class Grade(models.Model):
    grade = models.IntegerField(default='1')
    point = models.IntegerField(null=True)
