from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    '''Admin View for Channel'''

    list_display = ('id', 'user', 'channel_name', 'channel_desc', 'create_at')
    list_per_page = 10


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    '''Admin View for Video'''

    list_display = ('id', 'user', 'channel', 'thumbnail',
                    'video', 'title', 'public_view', 'video_desc', 'published_at')
    list_per_page = 10
