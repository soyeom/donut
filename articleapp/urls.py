from django.contrib import admin
from django.urls import path

from articleapp.views import detail, article, listing, update
from django.conf.urls.static import static
from django.conf import settings

app_name = 'articleapp'

urlpatterns = [
     path('admin/', admin.site.urls),
     path('create/', article, name='create'),
     path('', detail, name='detail'),
     path('create/<int:pk>/', listing, name="listing"),
     path('create/update/', update),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)