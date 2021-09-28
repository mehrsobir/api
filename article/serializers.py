from rest_framework import serializers
from .models import Article, Category, Type
from django.contrib.auth.models import User


class ArtSerialiser(serializers.ModelSerializer):
    # type = serializers.SerializerMethodField('get_type')
    # author = serializers.SerializerMethodField('get_author')
    # category = serializers.SerializerMethodField('get_category')

    class Meta:
        model = Article
        fields = ('id', 'author', 'title', 'slug', 'annotation', 'text', 'source', 'type', 'category',
                  'pubdate', 'updated', 'views',)

    # def get_author(self, article):
    #     username = article.author.user_name
    #     return username

    # def get_type(self, article):
    #     type = article.type.type
    #     return type
    #
    # def get_category(self, article):
    #     type = article.category.category
    #     return type

