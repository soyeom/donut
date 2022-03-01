from django.urls import path
from django.views.generic import TemplateView

app_name = 'introapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='introapp/list.html'), name='list')
]