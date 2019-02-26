from django import forms
from myblog.models import Post, Comment
from django.core import validators

class PostForm(forms.ModelForm):

    # def _post_clean(self):
    #     print('validation post details')
    #     total_clean_data = super().clean()
    #     inputpost = total_clean_data['author']
    #     if inputpost[0].lower()!='d':
    #         raise forms.ValidationError('Post should be starts with d latter')

    class Meta:
        model = Post
        fields = ('author', 'title', 'text',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
