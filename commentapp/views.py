from django.urls import reverse
from django.views.generic import CreateView, DeleteView
from django.utils.decorators import method_decorator
from articleapp.models import Article
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment
from commentapp.decorators import comment_ownership_required

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        if self.request.POST['comment_pk'] != '':
            temp_comment.parent = Comment.objects.get(pk=self.request.POST['comment_pk'])
        else:
            temp_comment.parent = None
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})


# class ReCommentCreateView(CreateView):
#     model = ReComment
#     form_class = ReCommentForm
#     template_name = 'commentapp/createRecomment.html'
#
#     def form_valid(self, form):
#         re_comment = form.save(commit=False)
#         re_comment.writer = self.request.user
#         re_comment.comment = Comment.objects.get(pk=self.request.POST['comment_pk'])
#         re_comment.save()
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})


@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk })