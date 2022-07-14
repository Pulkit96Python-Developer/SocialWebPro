from django.db import models
from django.contrib.auth.models import AbstractUser

class SignUp(models.Model):
    Email=models.EmailField(max_length=50,unique=True)
    Password=models.CharField(max_length=20)
    Verified=models.BooleanField(default=False)
    # Verification_Status=models.CharField(max_length=20,default='Not Verified')
    token=models.CharField(max_length=200)
    # is_email_verified=models.BooleanField(default=False)

    def __repr__(self) -> str:
        return self.Email

# class SocialApp(models.Model):
#     Provider='Google'
#     Name='login_app'
#     Client_id='64557264144-t74g10cjcri3l5jt4djpf42hsfjdarq7.apps.googleusercontent.com'
#     Secret_key='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'