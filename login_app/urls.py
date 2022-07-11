from django.urls import path
from login_app import views


urlpatterns=[
    # path('',views.LoginPage,name='login_form'),
    path('',views.UserLogin,name='login_app_urls'),
    path('Verify_token/',views.Verify_token,name='Verify_token')
    ]

