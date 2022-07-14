from django.urls import path
from Instagram import views


urlpatterns=[path('',views.Home,name='Instagram Investigation'),
path('getuserdetails/',views.GetUserDetails,name='Get User Details'),
]