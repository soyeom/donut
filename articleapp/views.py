import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Q

import articleapp
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm, PriceCreationForm
from articleapp.models import Article, Campaign


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:list')


def Camp(request):

    amount_sum = sum(Campaign.objects.filter(participants_id__exact=request.POST['text']))

    if (int(request.POST['each_amount']) <= int(request.POST['price'])) and (amount_sum <= int(request.POST['price'])):
        if request.method == 'POST':
            campaign = Campaign()
            campaign.amount = request.POST['each_amount']
            campaign.state = request.POST['state']
            campaign.participants_id = request.user.id
            campaign.article_id = request.POST['article_id']
            campaign.save()

            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_refferer_not_found'))
        else:
            return render(request, '/')
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_refferer_not_found'))


def deleteCamp(request):
    if request.method == 'POST':
        campaign = Campaign.objects.filter(participants_id_id__exact=request.user.id,
                                         article_id__exact=request.POST['article_id'])
        campaign.delete()

        article = Article.objects.filter(id__exact=request.POST['article_id'])

        sum = int(request.POST['amount']) - int(request.POST['each_amount'])
        article.update(amount=sum)

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_refferer_not_found'))
    else:
        return render(request, '/')

class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['A'] = Campaign.objects.filter(participants_id__exact=self.request.user.id,
                                                                 article_id=self.object.id)
        context['abc'] = Campaign.objects.filter(participants_id__exact=self.request.user.id,
                                                                 article__state__in='abc')
        context['d']='d'
        context['all_A'] = Campaign.objects.filter(article_id__exact=self.object.id,
                                                                 article__state='a')
        context['all'] = Campaign.objects.filter(article_id__exact=self.object.id)

        context['all_C'] = Campaign.objects.filter(article_id__exact=self.object.id,
                                                                 article__state='c')
        return context


class ArticleListView(ListView):
    model = Article
    template_name = 'articleapp/list.html'
    paginate_by = 9
    context_object_name = 'article_list'

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        article_list = Article.objects.order_by('-id')

        if search_keyword:
            if len(search_keyword) > 1:
                search_article_list = article_list.filter(title__icontains=search_keyword)

                return search_article_list
            else:
                messages.error(self.request, '2글자 이상 입력해주세요')
        return article_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_keyword = self.request.GET.get('q', '')

        if len(search_keyword) > 1:
            context['q'] = search_keyword

        return context

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class PriceCreateView(CreateView):
    model = Article
    form_class = PriceCreationForm
    context_object_name = 'target_campaign'
    template_name = 'articleapp/price.html'
    success_url = reverse_lazy('articleapp:list')

    def post(self, request, *args, **kwargs):
        article = Article.objects.filter(id__exact=self.request.POST.get('text'))
        article.update(state='c')
        campaign = Campaign.objects.filter(title_id_id__exact=self.request.POST.get('text'))
        campaign.update(state='c')
        return redirect('articleapp:list')


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articleapp:list')

    template_name = 'articleapp/delete.html'
