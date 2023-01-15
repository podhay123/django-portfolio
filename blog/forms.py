from django.forms import ModelForm
from django import forms
from blog.models import Coment


class upload_form(ModelForm):
    username = forms.TextInput()
    content = forms.TextInput()
    postnumer = forms.TextInput()

    class Meta:
        model = Coment
        fields = ["username", "content", "postnumer"]
