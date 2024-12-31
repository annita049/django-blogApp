from django.contrib import admin
from .models import Blog
from .models import Profile
# Register your models here.

admin.site.register(Blog)

admin.site.register(Profile)

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'profile_picture')