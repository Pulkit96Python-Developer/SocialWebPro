from django.shortcuts import render
from django.views.generic.edit import FormView
from signup_app import forms
from signup_app import models

# Create your views here.

def Home(request):
    # model_obj=models.SignUp.objects.all()
    # for i in model_obj:
    #     i.delete()
    # print('objects deleted')
    form_obj=forms.SignUpForm()
    return render(request,'home.html',{'form':form_obj})

def Errors(request):
    return render(request,'socialaccount/authentication_error.html')
