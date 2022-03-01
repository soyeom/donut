from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView


class IntroListView(ListView):
    context_object_name = 'intro_list'
    template_name = 'introapp/list.html'
    paginate_by = 3

