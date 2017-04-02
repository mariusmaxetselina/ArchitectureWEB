from django import forms
from django.contrib.auth import authenticate,login

class LoginForm(forms.Form):
	pseudo = forms.CharField(label="", help_text="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(label="", help_text="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))



class RegisterForm(forms.Form):
	username = forms.CharField(required = True, label="", help_text="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(required = True, label="", help_text="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	password_verif =forms.CharField(required = True, label="", help_text="", widget=forms.PasswordInput(attrs={'placeholder': 'Password again'}))
	email = forms.EmailField(required = True, label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
