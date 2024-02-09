from django import forms
from .models import *
from django.contrib.auth.models import User

class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'email'}))
    first_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'first name'}))
    last_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'last name'}))
    password_1 = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'password'}))
    password_2 = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'password again'}))

    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('User Exist')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email Exits')
        return email

    def clean_password_2(self):
        password1 = self.cleaned_data['password_1']
        password2 = self.cleaned_data['password_2']
        if password1 != password2:
            raise forms.ValidationError('Password not match')

        if len(password1) < 8:
            raise forms.ValidationError('password is less than 8 characters')

        if not any(item.isupper() for item in password2):
            raise forms.ValidationError('the password must have at least one capital letter')
        return password1


class UserLoginForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'password'}))


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address']


