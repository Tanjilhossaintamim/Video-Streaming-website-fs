from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    comment=forms.CharField(label='',required=True,widget=forms.TextInput(attrs={'placeholder':'Write Your Comment Here !'}))
    class Meta:
        model = Comment
        fields = ['comment']
