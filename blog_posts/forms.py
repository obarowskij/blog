from django import forms
from django.forms import fields, widgets,Textarea
from .models import comment,post
class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = "name","content"

class createPostForm(forms.ModelForm):
    class Meta:
        model = post
        exclude = "date","tags","slug","author"

class registerUserForm(forms.Form):
    name = forms.CharField(max_length=40)
    password = forms.CharField(max_length=30)
    password2 = forms.CharField(max_length=30)
    email = forms.EmailField()

class loginUserForm(forms.Form):
    mail = forms.EmailField(max_length=40)
    password = forms.CharField(max_length=30)