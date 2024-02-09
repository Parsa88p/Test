from . models import Profile
from django.contrib import admin

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'address']

admin.site.register(Profile,ProfileAdmin)