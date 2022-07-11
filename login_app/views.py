from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from login_app import forms,serializers
from rest_framework.response import Response
from signup_app import models

# Create your views here.


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
                # print(type(user_obj.Verification_Status))
                # return HttpResponse(user_obj.Verification_Status)
                if user_obj.Verified:
                    print(user_obj.Verified)
                    return render(request,'UserProfile/profile.html',{'name':form_data['Email']})
                else:
                    # return HttpResponse('Hello')
                    return redirect('Verify_token/')

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
    model_obj=models.SignUp()
    try:
        model_obj=models.SignUp.objects.get(token=form_token)
        # return HttpResponse(model_obj.Email)
        model_obj.Verified=True
        model_obj.save()
        # return HttpResponse('new verification status= '+model_obj.Verified)
        print(model_obj.Verified)
        return render(request,'UserProfile/profile.html')
    except:
        return render(request,'Verify_token.html',{'name':model_obj.Email})