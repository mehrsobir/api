from rest_framework import serializers
from users.models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


# from rest_framework import serializers
# from .models import Profile
# from django.contrib.auth.models import User
#
#
# class UserSerialiser(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         # fields = '__all__'
#         fields = ('username', 'first name', 'last name', 'email address',)
#
#
# class ProfileSerialiser(serializers.ModelSerializer):
#     username = serializers.SerializerMethodField('get_username')
#     class Meta:
#         model = Profile
#         # fields = '__all__'
#         fields = ('username', 'affiliation', 'address', 'phone', 'image',)
#
#     def get_username(self, profile):
#         username = profile.user.username
#         return username

