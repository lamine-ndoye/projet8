from django.db.models import fields
from django.forms.widgets import TextInput, Textarea
from django import forms
from blog.models import article

# from blog.models import comment

# from .models import Comment




class SearchPost(forms.Form):
    query = forms.CharField(max_length=250)

    class Meta:
        fields = ['query']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = article
        fields = ("titel","details","category")

                