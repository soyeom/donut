from django.urls import path
from .views import IntroListView

app_name = 'introapp'

urlpatterns = [
    path('home/', IntroListView.as_view(), name='home'),
]