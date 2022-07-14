from django.urls import path
from Linkedin import views

urlpatterns=[path('',views.Home,name='LinkedIn Home')]