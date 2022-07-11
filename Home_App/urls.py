from django import views
from django.urls import path
from Home_App import views

urlpatterns=[
    path('',views.Home,name='HomePage'),
    path('errors/',views.Errors,name='errors')
]