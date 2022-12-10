from django.core.exceptions import ValidationError
from django.forms import ModelForm

from frontend.models import News


class NewsForm(ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'master' in title:
            raise ValidationError("stop words in title")
        return title

    def clean(self):
        data = self.cleaned_data
        if len(data['title']+data['anons']) < 10:
                raise ValidationError("stop words in title")
        return data
    class Meta:
        model = News
        fields = '__all__'