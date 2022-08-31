from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from articleapp.models import Article, Campaign
from .models import donation_organization


class IntroListView(ListView):
    model = Article
    context_object_name = 'intro_list'
    template_name = 'introapp/home.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_article'] = Article.objects.order_by('-hit')[:5]
        campaign = Campaign.objects.filter(participants_id=self.request.user.id, state__in='abc').values('article_id',
                                                                                                         'state')
        if campaign:
            context['state'] = campaign[0]['state']
            article = Article.objects.get(id=campaign[0]['article_id'])
            context['campaign_title'] = article.title
        return context


def region_search(request):
    if request.method == "GET":
        query = request.GET.getlist('keyword')
        matchingresult = donation_organization.objects.filter(region__icontains=query)

    return render(request, 'introapp/societyinfo.html', {'matchingresult': matchingresult})


def societyinfo(request):
    return render(request, 'introapp/societyinfo.html')


class SocietyInfoView(ListView):
    model = User
    template_name = 'introapp/societyinfo.html'
