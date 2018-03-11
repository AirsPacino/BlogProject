from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """内部类"""
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
