from rest_framework import serializers
from signup_app import models

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.SignUp
        fields=['Email','Password']

    # def create(self, validated_data):
    #     return super().create(validated_data)

    def validate_password(self, attrs):
        if len(attrs)>20:
            raise serializers.ValidationError('Maximum password length is 20')
        else:
            return attrs