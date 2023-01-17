from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView
from django.contrib import messages

from commentapp.forms import CommentCreationForm

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm, PriceCreationForm, ArticlereceiptForm
from articleapp.models import Article, Campaign, PriceCategory, ArticleCategory

from introapp.models import Society


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView1(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create_donate.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.writer = self.request.user
        article.category = ArticleCategory.objects.get(name="기부")
        article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView2(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create_volunteer.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.writer = self.request.user
        article.category = ArticleCategory.objects.get(name="봉사")
        article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView3(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create_goods.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.writer = self.request.user
        article.category = ArticleCategory.objects.get(name='공구')
        article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


def Camp(request):
    if request.method == 'POST':
        campaign = Campaign()
        campaign.amount = request.POST['amount']
        campaign.participants_id = request.user.id
        campaign.article_id = request.POST['article_id']
        campaign.state = request.POST['state']
        article = Article.objects.get(id=campaign.article_id)
        article.total_amount = article.total_amount + int(campaign.amount)
        if article.price >= article.total_amount:
            campaign.save()
            article.save()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_refferer_not_found'))
    else:
        return render(request, '/')


def deleteCamp(request):
    if request.method == 'POST':
        campaign = Campaign.objects.get(participants_id__exact=request.user.id,
                                        article_id__exact=request.POST['article_id'])
        article = Article.objects.get(id=campaign.article_id)
        article.total_amount = article.total_amount - int(campaign.amount)
        article.save()
        campaign.delete()

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

        if Campaign.objects.filter(participants_id__exact=self.request.user.id, article_id=self.object.id):
            context['A'] = Campaign.objects.get(participants_id__exact=self.request.user.id,
                                                article_id=self.object.id)

        context['abc'] = Campaign.objects.filter(participants_id__exact=self.request.user.id,
                                                 state__in='abc')
        context['all_A'] = Campaign.objects.filter(article_id__exact=self.object.id,
                                                   state='a')
        context['all'] = Campaign.objects.filter(article_id__exact=self.object.id)

        context['all_C'] = Campaign.objects.filter(article_id__exact=self.object.id,
                                                   state='c')
        context['all_D'] = Campaign.objects.filter(article_id__exact=self.object.id,
                                                   state='d')
        return context

    def post(self, request, pk, *args, **kwargs):
        article = Article.objects.get(id__exact=request.POST['article_id'])
        campaign = Campaign.objects.filter(article_id=article.id)
        campaign.update(state='d')

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form, **kwargs)
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_refferer_not_found'))


class ArticleListView1(ListView):
    model = Article
    template_name = 'articleapp/goods_list.html'
    paginate_by = 9
    context_object_name = 'article_list'

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        article_list = Article.objects.filter(category_id=3).order_by('-id')

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


class ArticleListView2(ListView):
    model = Article
    template_name = 'articleapp/donate_list.html'
    paginate_by = 9
    context_object_name = 'article_list'

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        article_list = Article.objects.filter(category_id=1).order_by('-id')

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


class ArticleListView3(ListView):
    model = Article
    template_name = 'articleapp/volunteer_list.html'
    paginate_by = 9
    context_object_name = 'article_list'

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        article_list = Article.objects.filter(category_id=2).order_by('-id')

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
    model = PriceCategory
    form_class = PriceCreationForm
    context_object_name = 'price_category'
    template_name = 'articleapp/price.html'

    def get_context_data(self, **kwargs):
        context = super(PriceCreateView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        return context

    def post(self, request, pk, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        article = Article.objects.get(id__exact=pk)
        campaign = Campaign.objects.filter(article_id__exact=article.id)
        price = article.price

        if form.is_valid:
            pricecategory = form.save(commit=False)
            pricecategory.article_id = pk
            campaign.update(state='c')

            if price == pricecategory.food + pricecategory.shelter + pricecategory.clothing:
                pricecategory.save()
                return redirect('/articles/detail/' + str(pk))
            else:
                return redirect('/articles/detail/' + str(pk))

    def get_success_url(self):
        return reverse('articleapp:price')


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticlereceiptView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticlereceiptForm
    template_name = 'articleapp/receipt.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'



def donate_list(request):
    return reverse('articleapp:donate_list')

