from django.urls import path
from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleListView

app_name = "articleapp"

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
]