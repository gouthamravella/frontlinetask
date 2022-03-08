from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=45)
    password = forms.CharField(max_length=45, widget=forms.PasswordInput)
    