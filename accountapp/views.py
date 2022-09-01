from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from django.views.generic.list import MultipleObjectMixin

import articleapp
from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm, CampCreationForm, LoginForm

from articleapp.models import Article, Campaign, PriceCategory
from django.core.paginator import Paginator

has_ownership = [account_ownership_required, login_required]


class ArticleListView(ListView):
    model = Article
    template_name = 'accountapp/mypost.html'
    paginate_by = 10
    context_object_name = 'article_list'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(AccountDetailView, self).get_context_data(**kwargs)
        context['A'] = Article.objects.filter(writer__exact=self.request.user.id)

        context['a'] = Campaign.objects.filter(participants_id__exact=self.request.user.id,
                                                                 state__exact='a')
        context['b'] = Campaign.objects.filter(participants_id__exact=self.request.user.id,
                                                                 state__exact='b')
        context['c'] = Campaign.objects.filter(participants_id__exact=self.request.user.id,
                                                                 state__exact='c')
        context['d'] = Campaign.objects.filter(participants_id__exact=self.request.user.id,
                                                                 state__exact='d')
        context['abc'] = Campaign.objects.filter(participants_id__exact=self.request.user.id,
                                               state__in='abc'),
        context['bcd'] = Campaign.objects.filter(participants_id__exact=self.request.user.id,
                                                 state__in='bcd')
        context['sum']=0
        if context['bcd']:
            for amount in context['bcd']:
                amount.amount
                context['sum'] = context['sum'] + amount.amount
            context['sum'] = int(context['sum']/100)

        if context['c']:
            context['Campaign'] = Campaign.objects.get(participants_id__exact=self.request.user.id,
                                                                 state__exact='c')
            if context['Campaign']:
                context['amount'] = Article.objects.get(id__exact=context['Campaign'].article_id)
                context['category'] = PriceCategory.objects.get(article_id__exact=context['Campaign'].article_id)

        return context


class AccountDetailView2(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/mypost.html'

    def get_context_data(self, **kwargs):
        context = super(AccountDetailView2, self).get_context_data(**kwargs)
        context['Article'] = articleapp.models.Article.objects.filter(writer__exact=self.request.user.id)
        context['Campaign'] = articleapp.models.Campaign.objects.all()


        return context


class AccountDetailView3(DetailView):
    model = User
    context_object_name = 'target'
    template_name = 'accountapp/mycampaign.html'

    def get_context_data(self, **kwargs):
        context = super(AccountDetailView3, self).get_context_data(**kwargs)
        context['Campaign'] = articleapp.models.Campaign.objects.filter(participants_id__exact=self.request.user.id, state='d')
        context['Article'] = articleapp.models.Article.objects.all()
        return context

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
            user.save()
            return redirect('accountapp:login')
    return render(request, 'accountapp/create.html')


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'


def loging(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = auth.authenticate(request, username=username, password=password)
    #     if user is not None:
    #         auth.login(request, user)
    #         return redirect('introapp:home')
    #     else:
    #         return render(request, 'accountapp/login.html')
    #
    # else:
    #     return render(request, 'accountapp/login.html')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():  # form 검증
            username = form.cleaned_data['username']  # form에서 data 가져오기
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('introapp:home')
        return HttpResponse('Login failed. Try again.')  # 에러
    else:
        form = LoginForm()
        return render(request, 'accountapp/login.html')

