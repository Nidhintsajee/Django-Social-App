from .models import Post, Comment
from django import forms

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('status', 'image','description',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')