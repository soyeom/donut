from django.urls import path
from .views import IntroListView

app_name = 'introapp'

urlpatterns = [
    path('list/', IntroListView.as_view(), name='list'),
]