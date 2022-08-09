from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True, blank=True)
    content = models.TextField(null=True)
    price = models.IntegerField(default=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Campaign(models.Model):
    Participants = models.IntegerField()
    title_id = models.IntegerField()
    amount = models.IntegerField(default=0, null=False)
    price = models.IntegerField(default=0, null=False)
    state = models.CharField(max_length=1, default='a')
