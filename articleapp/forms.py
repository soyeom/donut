from django.forms import ModelForm

from articleapp.models import Article, Price


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'price', 'image', 'content']

class PriceCreationForm(ModelForm):
    class Meta:
        model = Price
        fields = ['food', 'clothing', 'shelter']