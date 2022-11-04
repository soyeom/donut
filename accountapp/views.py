from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from accountapp.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.views.generic import View
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView, FormView
from django.views.generic.list import MultipleObjectMixin

import articleapp
from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm, CampCreationForm

from articleapp.models import Article, Campaign, PriceCategory
from accountapp.models import User, Grade
from django.core.paginator import Paginator
from django.contrib.auth.hashers import check_password

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
        context['sum'] = 0
        if context['bcd']:
            for amount in context['bcd']:
                amount.amount
                context['sum'] = context['sum'] + amount.amount
            context['sum'] = int(context['sum'] / 100)

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
        context['Campaign'] = articleapp.models.Campaign.objects.filter(participants_id__exact=self.request.user.id,
                                                                        state='d')
        context['Article'] = articleapp.models.Article.objects.all()
        return context


class signup(View):
    model = User
    template_name = 'authentication/login.html'

    def get(self, request):
        return render(request, 'accountapp/create.html')

    def post(self, request):
        if request.POST['password1'] == request.POST['password2']:
            if User.objects.filter(id=request.POST['id']).exists():
                singup_username_errMsg = "* 이미 존재하는 아이디입니다."
                return render(request, 'accountapp/create.html', {"singup_username_errMsg": singup_username_errMsg})
            else:
                user = User()
                user.id = request.POST.get('id', False)
                user.password = request.POST.get('password1', False)
                user.username = request.POST.get('username', False)
                user.email = request.POST.get('email', False)
                user.save()
            return redirect('accountapp:login')

        else:
            if not (request.POST['password1']):
                singup_password1_errMsg = "* 비밀번호란에 비밀번호를 입력해주세요"
                return render(request, "accountapp/create.html", {"singup_password1_errMsg": singup_password1_errMsg})

            else:
                if not (request.POST['password2']):
                    singup_password2_errMsg = "* 비밀번호 재확인란에 비밀번호를 입력해주세요"
                elif not (request.POST['password1'] and request.POST['password2']):
                    singup_password2_errMsg = "* 비밀번호와 비밀번호 재확인란에 비밀번호를 입력해주세요"
                else:
                    singup_password2_errMsg = "* 비밀번호와 비밀번호 재확인란의 비밀번호가 일치하지 않습니다"
                return render(request, "accountapp/create.html", {"singup_password2_errMsg": singup_password2_errMsg})


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


class LoginPageView(View):
    model = User
    template_name = 'authentication/login.html'

    def get(self, request):
        return render(request, 'accountapp/login.html')

    def post(self, request):
        username = request.POST.get('login_id', False)
        password = request.POST.get('login_pw', False)
        login_errMsg = None
        user = auth.authenticate(request, id=username, password=password)

        if username and password:
            if user is not None:
                auth.login(request, user)
                return redirect('introapp:home')
            else:
                login_errMsg = "* 아이디 또는 비밀번호가 일치하지 않습니다"
                return render(request, 'accountapp/login.html', {'login_errMsg': login_errMsg})
        else:
            if not (username and password):
                login_errMsg = "* 아이디와 비밀번호를 입력하세요"
            if (not username) and password:
                login_errMsg = "* 아이디를 입력하세요"
            if username and (not password):
                login_errMsg = "* 비밀번호를 입력하세요"
            return render(request, 'accountapp/login.html', {'login_errMsg': login_errMsg})