from django.urls import path
from .views import IntroListView, SocietyInfoView

app_name = 'introapp'

urlpatterns = [
    path('home/', IntroListView.as_view(), name='home'),
    path('societyinfo/', SocietyInfoView.as_view(), name='societyinfo'),

]