from django.shortcuts import render
from .models import Profile
from rest_framework import status, viewsets
from .serializers import UserSerialiser

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerialiser
    queryset = Profile.objects.all()
