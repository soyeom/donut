
app_name = 'introapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='introapp/list.html'), name='list')
]