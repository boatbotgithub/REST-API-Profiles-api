from rest_framework import serializers
from profiles_api import models

'''
serializer is a feature from the Django rest framework that allows you to
easily convert data inputs into Python objects and vice versa it's kind of similar to a django form which
you define and it has various fields that you want to accept for the input for you api
'''


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    ''' ModelSerializer ใช้ Class Meta ในการเชื่อมต่อกับ Model '''
    class Meta:
        model = models.UserProfile

        fields = ('id', 'email', 'name', 'password')


        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }



    '''Overloading'''
    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    '''override '''
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

        return user



class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile','status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only':True}}