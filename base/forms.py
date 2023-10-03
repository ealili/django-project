# forms.py

from django import forms


class UserMessageForm(forms.Form):
    user_message = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type something...'}))
