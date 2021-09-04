from rest_framework import serializers
from .models import Article


class artserialiser(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = (
            'title', 'type', 'category', 'pubdate', 'views',
        )