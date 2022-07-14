from django import forms
from Home_App import models


class SignUpForm(forms.ModelForm):
    class Meta:
        model=models.SignUp
        fields=['Email','Password']
        widgets = {
        'Password': forms.PasswordInput(),
    }

class VerifyEmail(forms.Form):
    Email=forms.EmailField()
