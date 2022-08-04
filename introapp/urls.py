from django.urls import path
from .views import IntroListView, societyinfo

app_name = 'introapp'

urlpatterns = [
    path('home/', IntroListView.as_view(), name='home'),
    path('societyinfo/',societyinfo,name='societyinfo'),
]