from django.urls import path
from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleListView, ArticleUpdateView, \
<<<<<<< HEAD
    ArticleDeleteView, Camp, deleteCamp, deliverystart
=======
    ArticleDeleteView, Camp, deleteCamp, PriceCreateView
>>>>>>> 8a34b4a2ed96209d88f9f70af35834c253232803

app_name = "articleapp"

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
    path('campaign/', Camp, name='campaign'),
    path('deletecamp/', deleteCamp, name='deletecamp'),
<<<<<<< HEAD
    path('deliverystart/', deliverystart, name='deliverystart'),
=======
    path('price/', PriceCreateView.as_view(), name='price'),
>>>>>>> 8a34b4a2ed96209d88f9f70af35834c253232803
]