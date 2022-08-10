from django.forms import ModelForm

from articleapp.models import Article, Campaign


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'price', 'image', 'content']

class PriceCreationForm(ModelForm):
    class Meta:
        model = Campaign
        fields = ['food', 'clothing', 'shelter']