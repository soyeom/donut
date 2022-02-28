from django.db import models

# Create your models here.


class HelloWorld(models.Model): #models 클래스 상속
    text = models.CharField(max_length=225, null=False)