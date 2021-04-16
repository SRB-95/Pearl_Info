from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class userForm(UserCreationForm):
    # password2 lavel change
    password2 = forms.CharField(label = 'Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']