from django.shortcuts import render
from django.views.generic import ListView
from .models import Image

class IntroListView(ListView):
    model = Image
    context_object_name = 'intro_list'
    template_name = 'introapp/home.html'
    paginate_by = 3

def societyinfo(request):
    return render(request,'introapp/societyinfo.html')