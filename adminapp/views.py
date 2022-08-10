from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

import articleapp
from articleapp.models import Campaign, Article


class CampListView(ListView):
    model = Campaign
    template_name = 'adminapp/list.html'
    paginate_by = 12
    context_object_name = 'camp_list'

    def get_context_data(self, **kwargs):
        context = super(CampListView, self).get_context_data(**kwargs)
        context['A'] = User.objects.all()
        context['B'] = Article.objects.all()

        return context




def Campupdate(request):
    if request.method == 'POST':
        board = Campaign.objects.filter(id__exact=request.POST['id'])
        board.update(state=request.POST['state'])
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_refferer_not_found'))
    else:
        return render(request, '/')
