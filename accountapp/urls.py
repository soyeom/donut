from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import AccountDetailView, AccountUpdateView, AccountDeleteView, loging, signup

app_name = 'accountapp'

urlpatterns = [
    path('login/', loging, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', signup, name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]