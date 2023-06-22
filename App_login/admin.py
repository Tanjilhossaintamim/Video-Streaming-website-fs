from django.contrib import admin
from .models import User, Profile

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''Admin View for User'''

    list_display = ('id', 'email')
    list_per_page = 10


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Admin View for Profile'''

    list_display = ('id', 'username', 'full_name', 'phone',
                    'profile_pic', 'cover_photo', 'user',)
    list_per_page = 10
