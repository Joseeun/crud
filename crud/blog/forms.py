from django import forms
from .models import Post,Comment #Comment 기능 추가!

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'writer', 'body']

# CommentForm 추가
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']