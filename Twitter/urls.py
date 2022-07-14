from django.urls import path
from Twitter import views

urlpatterns=[path('',views.TwitterDataHomepage,name='FollowingData'),
path('followers/',views.GetFollowers,name='TwitterFollowers')
]