from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=10)
    user_pswd1 = models.CharField(max_length=10)
    user_pswd2 = models.CharField(max_length=10)