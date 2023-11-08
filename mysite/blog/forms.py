from django import forms
from .models import Post, Comment, Tag, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'head_image', 'file_upload', 'category', 'tags']

    tags = forms.CharField(max_length=50, required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    
class SearchForm(forms.Form):
    query = forms.CharField()