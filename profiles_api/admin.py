from django.contrib import admin
from profiles_api import models
# Register your models here.

''' add models to in the Database '''
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
