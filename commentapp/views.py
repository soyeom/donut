from django.db.models.fields import json
from django.shortcuts import redirect
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

    def post(self, request):
        data = json.loads(request.body)
        user = request.user
        article_id = data.get('article', None)
        parent_id = data.get('parent', None)
        content = data.get('content', None)

        Comment.objects.create(
            user=user,
            article=Article.objects.get(id=article_id),
            parent_id=parent_id,
            content=content
        )





@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk })