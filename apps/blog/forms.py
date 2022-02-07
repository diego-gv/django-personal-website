from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(max_length=60, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Input your name or alias"
    }))
    body = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Type your comment"
    }))