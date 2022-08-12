from django.forms import ModelForm

from articleapp.models import Article, PriceCategory


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'price', 'image', 'content']

class PriceCreationForm(ModelForm):
    class Meta:
        model = PriceCategory
        fields = ['food', 'clothing', 'shelter']