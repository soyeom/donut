from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accountapp.models import User

# Register your models here.

@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ['id', 'grade']

