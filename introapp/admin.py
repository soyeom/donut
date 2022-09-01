from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Society


@admin.register(Society)
class Societyadmin(admin.ModelAdmin):
    list_display = ['society', 'region', 'latitude', 'longitude', 'content']
