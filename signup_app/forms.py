from ast import Pass
from dataclasses import fields
from django import forms
from signup_app import models


class SignUpForm(forms.Form):
        Email=forms.EmailField()
        Password=forms.CharField(widget=forms.PasswordInput())