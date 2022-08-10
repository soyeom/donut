from django.contrib import admin

# Register your models here.
from django.contrib import admin

from articleapp.models import Campaign


@admin.register(Campaign)
class PostAdmin(admin.ModelAdmin):
    list_display = ['Participants', 'title', 'amount','price','state']
    list_display_links = ['state']