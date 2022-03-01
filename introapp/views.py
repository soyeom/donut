from django.views.generic import ListView
from .models import Image

class IntroListView(ListView):
    model = Image
    context_object_name = 'intro_list'
    template_name = 'introapp/list.html'
    paginate_by = 3