from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from articleapp.models import Article, Campaign


class IntroListView(ListView):
    model = Article
    context_object_name = 'intro_list'
    template_name = 'introapp/home.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_article'] = Article.objects.order_by('-hit')[:5]
        context['campaign'] = Campaign.objects.filter(participants_id=self.request.user.id)
        return context

def societyinfo(request):
    return render(request, 'introapp/societyinfo.html')