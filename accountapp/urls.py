from django.contrib.auth.views import LogoutView
from django.urls import path
from accountapp.views import AccountDetailView, AccountUpdateView, AccountDeleteView, signup, ArticleListView, \
    AccountDetailView2, AccountDetailView3, LoginPageView, Activate

app_name = 'accountapp'

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', signup.as_view(), name='create'),
    path('activate/<str:uidb64>/<str:token>', Activate.as_view()),
    path('detail/#(?P<pk>[0-9]+)', AccountDetailView.as_view(), name='detail'),
    path('mypost/#(?P<pk>[0-9]+)', AccountDetailView2.as_view(), name='mypost'),
    path('mycampaign/#(?P<pk>[0-9]+)', AccountDetailView3.as_view(), name='mycampaign'),
    path('update/#(?P<pk>[0-9]+)', AccountUpdateView.as_view(), name='update'),
    path('delete/#(?P<pk>[0-9]+)', AccountDeleteView.as_view(), name='delete'),
]

# (?P<pk>[0-9]+)<int:pk>
