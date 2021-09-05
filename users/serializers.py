from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class UserSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            'user', 'affiliation', 'address', 'phone', 'image',
        )