from django.urls import path

from adminapp.views import CampListView, Campupdate, CampListView2

app_name = "adminapp"

urlpatterns = [
    path('list/',CampListView.as_view() , name='list'),
    path('update/', Campupdate, name='update'),
]