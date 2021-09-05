from rest_framework import serializers
from .models import Article, Category, Type
from django.contrib.auth.models import User


class ArtSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Article
        # fields = '__all__'
            # 'author', 'annotation', 'title', 'text', 'source', 'type', 'category', 'pubdate', 'updated', 'views',
        # )
        exclude = ['slug']

class CatSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
            # 'category',
        # )


class TypeSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'
            # 'type',
        # )

