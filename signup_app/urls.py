from django.urls import path
from signup_app import views

urlpatterns=[
    path('',views.signup.as_view(),name='User Sign Up'),
    path('signup/',views.signup.as_view(),name='signup_user'),
    ]