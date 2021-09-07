from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class UserSerialiser(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'first name', 'last name', 'email address',)


class ProfileSerialiser(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ('username', 'affiliation', 'address', 'phone', 'image',)

    def get_username(self, profile):
        username = profile.user.username
        return username

