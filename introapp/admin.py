from django.contrib import admin

# Register your models here.
from django.contrib import admin

from introapp.models import Society


@admin.register(Society)
class PostAdmin(admin.ModelAdmin):
    list_display = ['society', 'region', 'latitude', 'longitude', 'content']