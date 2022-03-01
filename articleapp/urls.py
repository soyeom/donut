from django.conf.urls.static import static
from django.urls import path

from articleapp.views import article, detail, listing, update
from django.conf import settings

app_name = "articleapp"

urlpatterns = [
    path('create/', article, name='create'),
    path('', detail, name='detail'),
    path('create/<int:pk>/', listing, name="listing"),
    path('create/update/', update),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)