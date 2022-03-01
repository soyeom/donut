from django.shortcuts import render, redirect
from .models import Article

def article(request):
    articlelist = Article.objects.all()
    return render(request, 'articleapp/create.html', {'articlelist': articlelist})

def detail(request):
    return render(request, 'articleapp/detail.html')

def listing(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articleapp/list.html', {'article': article})

def update(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article = Article.objects.create(
                title=request.POST['title'],
                content=request.POST['content'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article = Article.objects.create(
                title=request.POST['title'],
                content=request.POST['content'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/articles/create')
    return render(request, 'articleapp/update.html')