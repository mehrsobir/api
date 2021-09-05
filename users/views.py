from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status, viewsets
from .serializers import UserSerialiser, ProfileSerialiser


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerialiser
    queryset = User.objects.all()


class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerialiser
    queryset = Profile.objects.all()
