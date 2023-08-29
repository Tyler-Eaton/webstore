from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': 'Your Username',
		'class': 'form-control'
	}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder': 'Your password',
		'class': 'form-control'
	}))

class SignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	username = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': 'Username',
		'class': 'form-control'
	}))
	email = forms.CharField(widget=forms.EmailInput(attrs={
		'placeholder': 'Email Address',
		'class': 'form-control'
	}))
	address = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': 'Address',
		'class': 'form-control'
	}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder': 'Password',
		'class': 'form-control'
	}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder': 'Repeat Password',
		'class': 'form-control'
	}))