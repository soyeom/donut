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

from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str

import articleapp
from accountapp.decorators import account_ownership_required

from accountapp.forms import AccountUpdateForm, CampCreationForm
from accountapp.text import message
from accountapp.token import account_activation_token

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
            if User.objects.filter(username=request.POST['username']).exists():
                singup_id_errMsg = "* 이미 존재하는 아이디입니다."
                return render(request, 'accountapp/create.html', {"singup_id_errMsg": singup_id_errMsg})
            else:
                user = User()
                user.id = request.POST.get('id', False)
                user.password = request.POST.get('password1', False)
                user.username = request.POST.get('username')
                user.email = request.POST.get('email')
                user.is_active = False
                user.save()

            current_site = get_current_site(request)
            domain = current_site.domain
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            message_data = message(domain, uidb64, token)

            mail_title = "이메일 인증을 완료해주세요"
            mail_to = user.email
            email = EmailMessage(mail_title, message_data, to=[mail_to])
            email.send()
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


class Activate(View):
    model = User

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)

            if account_activation_token.check_token(user, token):
                user.is_active = True
                user.save()

                return redirect('accountapp:login')

            return JsonResponse({"message": "AUTH FAIL"}, status=400)

        except ValidationError:
            return JsonResponse({"message": "TYPE_ERROR"}, status=400)
        except KeyError:
            return JsonResponse({"message": "INVALID_KEY"}, status=400)


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
        id = request.POST['login_id']
        password = request.POST['login_pw']
        login_errMsg = None

        # user = authenticate(request, username=username, password=password)
        try:
            user = User.objects.get(id=id, password=password)
        except:
            login_errMsg = "* 아이디와 비밀번호 둘 다 일치하지 않습니다."

            if id and password:
                user = request.user
                return redirect('introapp:home')
            else:
                login_errMsg = "* 아이디 또는 비밀번호가 일치하지 않습니다"
                return render(request, 'accountapp/login.html', {'login_errMsg': login_errMsg})
            # if user is not None:
            #     login(request, user)
            #     return redirect('introapp:home')
            # else:
            #     login_errMsg = "* 아이디 또는 비밀번호가 일치하지 않습니다"
            #     return render(request, 'accountapp/login.html', {'login_errMsg': login_errMsg})
            # if id == user.id:
            #    if password == user.password:
            #        login(request, user)
            #        return redirect('introapp:home')
            #    else:
            #        login_errMsg = "* 비밀번호가 일치하지 않습니다"
            #        return render(request, 'accountapp/login.html', {'login_errMsg': login_errMsg})

            # else:
            #    if password == user.password:
            #        login_errMsg = "* 아이디가 일치하지 않습니다"
            #    return render(request, 'accountapp/login.html', {'login_errMsg': login_errMsg})
        else:
            if not (id and password):
                login_errMsg = "* 아이디와 비밀번호를 입력하세요"
            if (not id) and password:
                login_errMsg = "* 아이디를 입력하세요"
            if id and (not password):
                login_errMsg = "* 비밀번호를 입력하세요"
            return render(request, 'accountapp/login.html', {'login_errMsg': login_errMsg})
