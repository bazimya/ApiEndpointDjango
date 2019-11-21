from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # profile_photo = models.ImageField(upload_to = 'profile/')
    bio = models.CharField(max_length =100)
    name = models.CharField(max_length =100, null=True)
    phone_number = models.PositiveIntegerField(null=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)

    @classmethod
    def get_profile(cls, user):
        profile = cls.objects.filter(user=user).first()
        return profile
    
    @classmethod
    def get_many_profiles(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

    @classmethod
    def get_profile_id(cls, user):
        profile = cls.objects.get(pk =user)
        return profile