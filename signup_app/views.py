from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from signup_app.forms import SignUpForm
from signup_app import serializers
from signup_app import models
from rest_framework.response import Response
from django.conf import settings
from django.core.mail import send_mail
import uuid

# Create your views here.

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
            message = f'Hi {form_data["Email"]}, thank you for registering with CYBER SAFE TECHNOLOGIES. Your verification code is: {model_obj.token}.\nPlease use this code to login'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form_data["Email"], ]
            print(email_from)
            print(recipient_list[0])
            send_mail( subject, message, email_from, recipient_list )
            
        else:
            return Response(seri_obj.errors)
        
        return Response('New User Created')

    