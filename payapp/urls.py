
from django.urls import path
from . import views

app_name = "payapp"

urlpatterns = [
    path('', views.index, name="index"),
    path('approval/', views.approval, name="approval"),
    path('charge/', views.chargeindex, name="charge"),
    path('chargeapproval/', views.chargeapproval, name="chargeapproval"),
]