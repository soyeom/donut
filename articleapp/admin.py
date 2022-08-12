from django.contrib import admin

# Register your models here.
from django.contrib import admin

from articleapp.models import Campaign, Article


@admin.register(Campaign)
class PostAdmin(admin.ModelAdmin):
    list_display = ['amount']
    list_display_links = ['amount']


@admin.register(Article)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'price', 'state']
    list_display_links = ['state']
