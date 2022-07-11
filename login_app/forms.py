from signup_app import models
from django import forms


class UserLogin(forms.ModelForm):
    class Meta:
        model=models.SignUp
        fields='__all__'
        widget={
        'password': forms.PasswordInput(),
    }