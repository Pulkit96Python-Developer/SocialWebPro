from django import views
from django.urls import path
from Home_App import views

urlpatterns=[
    path('',views.Home,name='HomePage'),
    path('signup/',views.signup.as_view(),name='signup_user'),
    path('login/',views.UserLogin,name='user_login'),
    path('login/VerifyToken/',views.Verify_token,name='VerifyToken'),
    path('VerifyEmail/',views.GetUserEmail.as_view(),name='VerifyEmail'),
    path('ResetPassword/',views.ResetPassword,name='ResetPassword'),
    path('Dashboard/',views.Dashboard,name='Dashboard'),
    # path('errors/',views.Errors,name='errors')
]