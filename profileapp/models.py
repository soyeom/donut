
from django.db import models
from accountapp.models import User

from accountapp.models import User

from django.db import models
from accountapp.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20,unique=True, null=True)
    message = models.CharField(max_length=100, null=True)