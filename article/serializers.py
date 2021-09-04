from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User


class ArtSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = (
            'author', 'title', 'text', 'type', 'category', 'pubdate', 'views',
        )

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

