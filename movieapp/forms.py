from django import forms
from django.contrib.auth.forms import UserCreationForm

class SubscriberForm(UserCreationForm):
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'})
    )