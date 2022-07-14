import json
from urllib import response
from django.shortcuts import render
from googleapiclient.discovery import build
import pandas as pd
import requests
import seaborn as sns
from rest_framework.views import APIView
from rest_framework.response import Response
from bs4 import BeautifulSoup
import re
from urllib import parse
from YouTube.models import YouTubeSearcher
from Home_App.models import SignUp

# Create your views here.

api_key='AIzaSyDkUccn2PTV6o8O7lbBz7JTP7pomtEY8y0'

class GetChannelActivites(APIView):
    def post(self,request):

        URL = request.data['ChannelURL']
        soup = BeautifulSoup(requests.get(URL).content, "html.parser")

        # We locate the JSON data using a regular-expression pattern
        data = re.search(r"var ytInitialData = ({.*});", str(soup)).group(1)

        # This converts the JSON data to a python dictionary (dict)
        json_data = json.loads(data)
        channel_id=json_data['header']['c4TabbedHeaderRenderer']['channelId']
        print(channel_id)
        # print("Joined:", stats["joinedDateText"]["runs"][1]["text"])
        print('channel_ID= ',channel_id)

        youtube_activity_data=requests.get(f"https://youtube.googleapis.com/youtube/v3/activities?part=snippet%2CcontentDetails&channelId={channel_id}&key={api_key}&HTTP/1.1")
        
        # json() method will convert the 'response' object into Python Dictionary
        activity_json=youtube_activity_data.json()
        # activity_data=json.loads(activity_json)
        youtube_searcher=YouTubeSearcher()
        user_email=SignUp.objects.get(Email=request.session['Email'])
        youtube_searcher.Searcher_Email=user_email.Email
        youtube_searcher.save()
        print(request.session['Email'])
        youtube_searcher=YouTubeSearcher()
        user_email=SignUp.objects.get(Email=request.session['Email'])
        youtube_searcher.Searcher_Email=user_email.Email
        youtube_searcher.save()
        return Response(activity_json)

class GetCaptions(APIView):
    def post(self,request):
        # URL = request.data['Video']
        print(request.data)
        url_data = parse.urlparse(f"{URL}")
        query = parse.parse_qs(url_data.query)
        video_id = query["v"][0]
        print(video_id)
        captions_request=requests.get(f"https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={video_id}&key={api_key}&HTTP/1.1")
        caption_data=captions_request.json()
        print(caption_data)
        youtube_searcher=YouTubeSearcher()
        user_email=SignUp.objects.get(Email=request.session['Email'])
        youtube_searcher.Searcher_Email=user_email.Email
        youtube_searcher.save()
        return Response(caption_data)

class GetChannelDetails(GetChannelActivites):
    def post(self,request):
        URL = request.data['ChannelURL']
        soup = BeautifulSoup(requests.get(URL).content, "html.parser")

        # We locate the JSON data using a regular-expression pattern
        data = re.search(r"var ytInitialData = ({.*});", str(soup)).group(1)

        # This converts the JSON data to a python dictionary (dict)
        json_data = json.loads(data)
        channel_id=json_data['header']['c4TabbedHeaderRenderer']['channelId']
        
        # print("Joined:", stats["joinedDateText"]["runs"][1]["text"])
        

        youtube_channel_details=requests.get(f"https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id={channel_id}&key={api_key}&HTTP/1.1")
        
        # json() method will convert the 'response' object into Python Dictionary
        details_json=youtube_channel_details.json()
        # activity_data=json.loads(activity_json)
        youtube_searcher=YouTubeSearcher()
        user_email=SignUp.objects.get(Email=request.session['Email'])
        youtube_searcher.Searcher_Email=user_email.Email
        youtube_searcher.save()
        print(request.session['Email'])
        youtube_searcher=YouTubeSearcher()
        user_email=SignUp.objects.get(Email=request.session['Email'])
        youtube_searcher.Searcher_Email=user_email.Email
        youtube_searcher.save()
        return Response(details_json)

class GetComments(APIView):
    def post(self,request):
        URL = request.data['VideoComments']
        url_data = parse.urlparse(f"{URL}")
        query = parse.parse_qs(url_data.query)
        video_id = query["v"][0]
        comments_request=requests.get(f"https://youtube.googleapis.com/youtube/v3/commentThreads?part=snippet%2Creplies&videoId={video_id}&key={api_key}&HTTP/1.1")
        comments_data=comments_request.json()
        youtube_searcher=YouTubeSearcher()
        user_email=SignUp.objects.get(Email=request.session['Email'])
        youtube_searcher.Searcher_Email=user_email.Email
        youtube_searcher.save()
        return Response(comments_data)

class GetChannelMembers(APIView):
    def post(self,request):

        URL = request.data['ChannelURL']
        soup = BeautifulSoup(requests.get(URL).content, "html.parser")

        # We locate the JSON data using a regular-expression pattern
        data = re.search(r"var ytInitialData = ({.*});", str(soup)).group(1)

        # This converts the JSON data to a python dictionary (dict)
        json_data = json.loads(data)
        channel_id=json_data['header']['c4TabbedHeaderRenderer']['channelId']
        # print("Joined:", stats["joinedDateText"]["runs"][1]["text"])

        youtube_activity_data=requests.get(f"https://www.googleapis.com/youtube/v3/members?&client_id=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&channelId={channel_id}")
        
        # json() method will convert the 'response' object into Python Dictionary
        activity_json=youtube_activity_data.json()
        # activity_data=json.loads(activity_json)
        youtube_searcher=YouTubeSearcher()
        user_email=SignUp.objects.get(Email=request.session['Email'])
        youtube_searcher.Searcher_Email=user_email.Email
        youtube_searcher.save()
        
        return Response(activity_json)

class VideoSearchResults(APIView):
    def post(self,request):
        Keyword = request.data['Keyword']
        video_request=requests.get(f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q={Keyword}&key={api_key}&HTTP/1.1")
        video_data=video_request.json()
        youtube_searcher=YouTubeSearcher()
        user_email=SignUp.objects.get(Email=request.session['Email'])
        youtube_searcher.Searcher_Email=user_email.Email
        youtube_searcher.save()
        return Response(video_data)

class GetVideoInformation(APIView):
    def post(self,request):
        URL = request.data['VideoInfo']
        url_data = parse.urlparse(f"{URL}")
        query = parse.parse_qs(url_data.query)
        video_id = query["v"][0]
        comments_request=requests.get(f"https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails&id={video_id}&key={api_key}&HTTP/1.1")
        comments_data=comments_request.json()
        youtube_searcher=YouTubeSearcher()
        user_email=SignUp.objects.get(Email=request.session['Email'])
        youtube_searcher.Searcher_Email=user_email.Email
        youtube_searcher.save()
        return Response(comments_data)

class GetVideoLanguages(APIView):
    def post(self,request):
        URL = request.data['VideoLanguages']
        url_data = parse.urlparse(f"{URL}")
        query = parse.parse_qs(url_data.query)
        video_id = query["v"][0]
        comments_request=requests.get(f"https://youtube.googleapis.com/youtube/v3/i18nLanguages?part=snippet&key={api_key}&HTTP/1.1")
        comments_data=comments_request.json()
        youtube_searcher=YouTubeSearcher()
        user_email=SignUp.objects.get(Email=request.session['Email'])
        youtube_searcher.Searcher_Email=user_email.Email
        youtube_searcher.save()
        return Response(comments_data)

class GetChannelSubscription(APIView):
    def post(self,request):
        URL = request.data['ChannelSubscriptions']
        soup = BeautifulSoup(requests.get(URL).content, "html.parser")

        # We locate the JSON data using a regular-expression pattern
        data = re.search(r"var ytInitialData = ({.*});", str(soup)).group(1)

        # This converts the JSON data to a python dictionary (dict)
        json_data = json.loads(data)
        channel_id=json_data['header']['c4TabbedHeaderRenderer']['channelId']
        
        # print("Joined:", stats["joinedDateText"]["runs"][1]["text"])
        

        channel_subscription_details=requests.get(f"https://youtube.googleapis.com/youtube/v3/membershipslevels?part=snippet&channelId={channel_id}&key={api_key}")
        
        # json() method will convert the 'response' object into Python Dictionary
        details_json=channel_subscription_details.json()
        # activity_data=json.loads(activity_json)
        youtube_searcher=YouTubeSearcher()
        user_email=SignUp.objects.get(Email=request.session['Email'])
        youtube_searcher.Searcher_Email=user_email.Email
        youtube_searcher.save()
        print(request.session['Email'])
        return Response(details_json)