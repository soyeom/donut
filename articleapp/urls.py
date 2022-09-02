from django.urls import path
<<<<<<< HEAD
from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleListView, ArticleUpdateView, \
    ArticleDeleteView, Camp, deleteCamp, PriceCreateView, ArticlereceiptView, ArticleCreateView3
=======
from articleapp.views import ArticleCreateView1, ArticleDetailView, ArticleListView, ArticleUpdateView, \
    ArticleDeleteView, Camp, deleteCamp, PriceCreateView, ArticlereceiptView
>>>>>>> a3d2fb65d0c63221795eaceab4fa90616ab7431a

app_name = "articleapp"

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='list'),
<<<<<<< HEAD
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('goods/', ArticleCreateView3.as_view(), name='goods'),
=======
    path('donate/', ArticleCreateView1.as_view(), name='donate'),
>>>>>>> a3d2fb65d0c63221795eaceab4fa90616ab7431a
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
    path('campaign/', Camp, name='campaign'),
    path('deletecamp/', deleteCamp, name='deletecamp'),
    path('receipt/<int:pk>', ArticlereceiptView.as_view(), name='receipt'),

    path('price/<int:pk>', PriceCreateView.as_view(), name='price'),

    ]