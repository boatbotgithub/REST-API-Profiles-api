from django.shortcuts import render
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters


''' for login '''
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

''' config permissions '''
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
#from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):

    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer

    '''
    กำหนดว่าจะรับ query มาจากไหน
    UserProfile.object6.all ก็คือรับทุกอย่าง ที่อยู่ใน UserProfile
    '''

    queryset = models.UserProfile.objects.all()
    # authentication_classes = (TokenAuthentication,)

    '''config UpdateOnwProfile in file premissions class'''
    permission_classes = (permissions.UpdateOwnProfile,)

    ''' add search come filters '''
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')



''' ObtainAuthToken'''
class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""

   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    '''กำหนดให้ผู้ที่ไม่มี Token นั้น อ่านได้อย่างเดียว'''
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile = self.request.user)
    
