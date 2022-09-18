from django.urls import path

from articleapp.views import ArticleCreateView1, ArticleDetailView, ArticleUpdateView, \
    ArticleDeleteView, Camp, deleteCamp, PriceCreateView, ArticlereceiptView, ArticleCreateView2, ArticleCreateView3, \
    ArticleListView1, ArticleListView2, ArticleListView3

from articleapp.views import ArticleCreateView1, ArticleDetailView, ArticleUpdateView, \
    ArticleDeleteView, Camp, deleteCamp, PriceCreateView, ArticlereceiptView


app_name = "articleapp"

urlpatterns = [
    path('goods_list/', ArticleListView1.as_view(), name='list'),
    path('donate_list/', ArticleListView2.as_view(), name='list'),
    path('volunteer_list/', ArticleListView3.as_view(), name='list'),

    path('create_donate/', ArticleCreateView1.as_view(), name='donate'),

    path('create_volunteer/', ArticleCreateView2.as_view(), name='volunteer'),

    path('create_goods/', ArticleCreateView3.as_view(), name='goods'),


    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
    path('campaign/', Camp, name='campaign'),
    path('deletecamp/', deleteCamp, name='deletecamp'),
    path('receipt/<int:pk>', ArticlereceiptView.as_view(), name='receipt'),

    path('price/<int:pk>', PriceCreateView.as_view(), name='price'),

    ]
