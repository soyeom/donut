from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password
from django.forms import ModelForm
from django import forms
from articleapp.models import Campaign

from django.contrib.auth.models import User

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].disabled = True


class CampCreationForm(ModelForm):
    class Meta:
        model = Campaign
        fields = ['amount']
