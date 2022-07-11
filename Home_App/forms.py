from dataclasses import fields
from django import forms
from signup_app import models


class SignUpForm(forms.ModelForm):
    class Meta:
        model=models.SignUp
        fields='__all__'
        widgets = {
        'password': forms.PasswordInput(),
    }