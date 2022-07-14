from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import tweepy
# Create your views here.


@api_view(['GET'])
def TwitterDataHomepage(request):
    return render(request,'TwitterHome.html')


@api_view(['POST'])
def GetFollowers(request):
    username=request.data['Username']
    Followers_List=list()
    # li=tweepy.API.get_followers(username)
    # print(li)
    for follower in tweepy.Cursor(tweepy.api.get_followers(screen_name=username)).items():
        Followers_List.append(follower)

    return Response(Followers_List)