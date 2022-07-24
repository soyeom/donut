from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from articleapp.models import Article
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)

    def get_success_url(self):
<<<<<<< HEAD
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})
=======
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk })
>>>>>>> 82780b8d0c878ee9f1ffa9bb22fd8258ebe81635
