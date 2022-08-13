from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import AccountDetailView, AccountUpdateView, AccountDeleteView, loging, signup, ArticleListView, AccountDetailView2, AccountDetailView3

app_name = 'accountapp'

urlpatterns = [
    path('login/', loging, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', signup, name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('mypost/<int:pk>', AccountDetailView2.as_view(), name='mypost'),
    path('mycampaign/<int:pk>', AccountDetailView3.as_view(), name='mycampaign'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]
