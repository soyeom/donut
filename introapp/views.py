from django.shortcuts import render

# Create your views here.

class IntroListView(ListView):
    model = Intro
    context_object_name = 'intro_list'
    template_name = 'introapp/list.html'
    paginate_by = 3

