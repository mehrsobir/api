from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class UserSerialiser(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
            # 'username', 'first name', 'last name', 'email address',
        # )


class ProfileSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
            # 'user', 'affiliation', 'address', 'phone', 'image',
        # )
