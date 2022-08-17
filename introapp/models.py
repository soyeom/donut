from django.db import models

# Create your models here.
from articleapp.models import Article


class Image(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField()

    def __str__(self):
        return self.title

