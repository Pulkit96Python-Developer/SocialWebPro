from django import http
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.edit import FormView
from Home_App import models
from django import forms
from django.http import HttpResponse
from rest_framework.views import APIView
from Home_App.forms import SignUpForm,VerifyEmail
from Home_App import serializers
from rest_framework.response import Response
from django.conf import settings
from django.core.mail import send_mail
import uuid
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.template.loader import render_to_string

# Create your views here.

def Home(request):
    form_obj=SignUpForm()
    return render(request,'home.html',{'form':form_obj})

def Errors(request):
    return render(request,'socialaccount/authentication_error.html')

class signup(APIView):
    def get(self,request):
        form_obj=SignUpForm()
        return render(request,'signup.html',{'form':form_obj})

    def post(self,request):
        form_data=request.data
        # return HttpResponse(form_data)
        seri_obj=serializers.SignUpSerializer(data=form_data)
        if seri_obj.is_valid():
            model_obj=models.SignUp()
            model_obj.Email=request.data['Email']
            model_obj.Password=request.data['Password']
            model_obj.Verified=False
            model_obj.token=str(uuid.uuid4())
            model_obj.save()
            request.session['user']=model_obj.Email
            subject = 'CyberSafe Verification E-mail'
            message = f'Hi {form_data["Email"]}, thank you for registering with CYBER SAFE TECHNOLOGIES. Your verification code is: {model_obj.token}.\nPlease visit {{127.0.0.1:8000/login/VerifyToken/}} and enter this token'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form_data["Email"], ]
            print(email_from)
            print(recipient_list[0])
            send_mail( subject, message, email_from, recipient_list )
            
        else:
            return Response(seri_obj.errors)
        
        return Response("'New user is created and Account Activation Token is sent to user's E-mail'")


@api_view(['GET'])
def LoginPage(request):
    form_obj=forms.UserLogin()
    return render(request,'login.html',{'form':form_obj})

@api_view(['POST'])
def UserLogin(request):
    form_data=request.data
    seri_obj=serializers.LoginSerializer(data=form_data)
    if seri_obj.is_valid():
        try:
            user_obj= models.SignUp.objects.get(Email=form_data['Email'])
            
            if user_obj.Password==form_data['Password']:
                
                if user_obj.Verified:
                    request.session['Email']=user_obj.Email
                    # print(user_obj.Verified)
                    return redirect('/Dashboard/')
                    return render(request,'profile.html',{'name':form_data['Email']})
                else:
                    return redirect('VerifyToken/')

            else:
                return Response('invalid password')
        except:
            return Response('This user does not exist')
    else:
        return Response(seri_obj.errors)

# the user will enter the verification token which he got on his E-mail
# this function will verify the user
def Verify_token(request):
    form_token=request.POST.get('Token')
    try:
        model_obj=models.SignUp.objects.get(token=form_token)
        model_obj.Verified=True
        model_obj.save()
        request.session['Email']=model_obj.Email
        # return HttpResponse('new verification status= '+str(model_obj.Verified))
        return redirect('/Dashboard/')
    except:
        return render(request,'Verify_token.html')

    
def Dashboard(request):
        return render(request,'profile.html',{'name':request.session['Email']})


#Reset Password function
class GetUserEmail(View):
    def get(self,request):
        form=VerifyEmail()
        return render(request,'Get_Email.html',{'form':form})
    
    def post(self,request):
        try:
            model_obj=models.SignUp.objects.get(Email=request.POST.get('Email'))
            if model_obj:
                request.session['Password_Reset_Email']=model_obj.Email
                return render(request,'Reset_Password.html')
        except:
            return HttpResponse("User with this Email doesn't exist")

def ResetPassword(request):
    Pwrd=request.POST.get('Password')
    CnfPwrd=request.POST.get('ConfirmPassword')
    try:
        Pwrd==CnfPwrd
        print('I ran')
        model_obj=models.SignUp.objects.get(Email=request.session['Password_Reset_Email'])
        # return HttpResponse('woooooo')
        model_obj.Password=Pwrd
        model_obj.save()
        subject = 'CyberSafe Verification E-mail'
        message = f'Click this link to login {{http://127.0.0.1:8000}}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [model_obj.Email, ]
        # print(email_from)
        # print(recipient_list[0])
        send_mail( subject, message, email_from, recipient_list )
        return HttpResponse('Your password has been reset, please visit your E-mail to get the login link')

    except:
        print(Pwrd)
        print(CnfPwrd)
        return HttpResponse("Password and Confirm Password Don't Match")