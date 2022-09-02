from django.urls import path
from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleListView, ArticleUpdateView, \
    ArticleDeleteView, Camp, deleteCamp, PriceCreateView, ArticlereceiptView, ArticleCreateView3

app_name = "articleapp"

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('goods/', ArticleCreateView3.as_view(), name='goods'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
    path('campaign/', Camp, name='campaign'),
    path('deletecamp/', deleteCamp, name='deletecamp'),
    path('receipt/<int:pk>', ArticlereceiptView.as_view(), name='receipt'),

    path('price/<int:pk>', PriceCreateView.as_view(), name='price'),

    ]