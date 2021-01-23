from django import forms
from webapp.models import Messages


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['message']


