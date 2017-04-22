from django import forms


class PostForm(forms.Form):
    post_content = forms.Textarea(max_length=200)