from importlib.resources import path
from django.urls import path
from YouTube import views
from django.views.generic import TemplateView
urlpatterns=[path('',TemplateView.as_view(template_name ='YouTube.html'),name='YouTubeHome'),
path('channelactivities/',views.GetChannelActivites.as_view(),name='ChannelActivities'),
path('GetCaptions/',views.GetCaptions.as_view(),name='GetCaptions'),
path('channeldetails/',views.GetChannelDetails.as_view(),name='ChannelDetails'),
path('videocomments/',views.GetComments.as_view(),name='GetVideoComments'),
path('getchannelmembers/',views.GetChannelMembers.as_view(),name='GetChannelMembers'),
path('searchvideo/',views.VideoSearchResults.as_view(),name='VideoSearchResults'),
path('videoinformation/',views.GetVideoInformation.as_view(),name='Video Information'),
path('videolanguages/',views.GetVideoLanguages.as_view(),name='Video Languages'),
path('channelsubscriptions/',views.GetChannelSubscription.as_view(),name='Channel Subscriptions'),
]