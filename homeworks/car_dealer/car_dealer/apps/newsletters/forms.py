from django.forms import ModelForm
from .models import NewsLetter


class NewsLetterModelForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']
