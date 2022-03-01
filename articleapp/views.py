from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article

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
        return reverse('articleapp:list', kwargs={'pk': self.object})

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articleapp/detail.html'

class ArticleListView(ListView):
    model = Article
    template_name = 'articleapp/list.html'
    paginate_by = 10
    ordering = ['-id']