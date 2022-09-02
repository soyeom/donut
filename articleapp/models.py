from django.contrib.auth.models import User
from django.db import models

class ArticleCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, related_name='articlecategory')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True, blank=True)
    content = models.TextField(null=True)
    price = models.IntegerField(default=0, null=False)
    total_amount = models.IntegerField(default=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    receipt = models.ImageField(upload_to='articlereceipt/', null=True, blank=True)
    hit = models.IntegerField(default=0, null=False)

    def update_hit(self):
        self.hit += 1
        self.save()

        return " "

    def __str__(self):
        return self.title


class Campaign(models.Model):
    participants = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='campaign', null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='campaign', null=True)
    amount = models.IntegerField(default=0, null=False)
    state = models.CharField(max_length=1, default='a')

class PriceCategory(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='pricecategory', primary_key=True)
    food = models.IntegerField(default=0, null=True, blank=True)
    clothing = models.IntegerField(default=0, null=True, blank=True)
    shelter = models.IntegerField(default=0, null=True, blank=True)

