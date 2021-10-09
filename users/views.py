from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format='json'):
        data = request.data
        if data["password1"] == data["password"]:
            serializer = CustomUserSerializer(data=data)
            if serializer.is_valid():
                user = serializer.save()
                if user:
                    json = serializer.data
                    return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token = Token.objects.get(user=user)
        return Response({"token": token.key, "user_id": user.pk, 'user_name': user.user_name}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        django_logout(request)
        return Response(status=204)

