from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from .forms import ArticleCreationForm
from .models import Article

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

    def Article(request):
        articlelist = Article.objects.all()
        return render(request, 'articleapp/create.html', {'articlelist': articlelist})

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'

    def Detail(request):
        return render(request, 'articleapp/detail.html')