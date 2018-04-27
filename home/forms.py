from django import forms

class SingupForm (forms.Form):
    full_name=forms.CharField(max_length=30)
    email=forms.CharField(max_length=30)
    user_name=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput)
