from django.contrib import admin
from .models import Like, Comment, Subscribe, Views

# Register your models here.


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    '''Admin View for Like'''

    list_display = ('id', 'user', 'video')
    list_per_page = 10


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Admin View for Comment'''

    list_display = ('id', 'user', 'comment', 'video', 'comment_date')
    list_per_page = 10


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    '''Admin View for Subscribe'''

    list_display = ('id', 'subsciber', 'channel')
    list_per_page = 10


@admin.register(Views)
class LikeAdmin(admin.ModelAdmin):
    '''Admin View for Like'''

    list_display = ('id', 'viewer', 'video')
    list_per_page = 10
