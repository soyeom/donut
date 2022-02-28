from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from .forms import ArticleCreationForm
from .models import Article


def article(request):
    articlelist = Article.objects.all()
    return render(request, 'articleapp/create.html', {'articlelist': articlelist})

def detail(request):
    return render(request, 'articleapp/detail.html')

def listing(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articleapp/list.html', {'article': article})