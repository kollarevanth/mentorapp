from django import forms
from onlineapp.models import *
class signUp(forms.Form):

        first_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter'}))


        last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter'}))
        username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter'}))
        email= forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'enter'}))
        password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter'}))


class loginForm(forms.Form):
        username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter'}))
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter'}))