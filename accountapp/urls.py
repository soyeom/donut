from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

app_name = "accountapp"

<<<<<<< HEAD
urlpatterns = [
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
=======
urlpatterns = {
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

}
>>>>>>> 2ece017ff6539ebe04509570f9710b79f508431b
