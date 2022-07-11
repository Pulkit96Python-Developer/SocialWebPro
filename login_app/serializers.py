from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    Email=serializers.CharField()
    Password=serializers.CharField()