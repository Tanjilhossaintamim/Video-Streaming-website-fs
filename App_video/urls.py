from django.urls import path
from . import views


app_name = 'App_video'

urlpatterns = [
    path('', views.AllVideos.as_view(), name='home'),
    path('video_details/<pk>/', views.video_details, name='video_details'),
    path('create_channel/', views.create_channel, name='create_channel'),
    path('edit_channel/', views.edit_channel, name='edit_channel'),
    path('channel/', views.channel_view, name='channel'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('edit_video/<pk>/', views.edit_video, name='edit_video'),
    path('delete_video/<pk>/', views.delete_video, name='delete_video'),
    path('make_private/<pk>/', views.make_privet_video, name='make_private'),
    path('make_public/<pk>/', views.make_video_public, name='make_public'),
    path('show_channel/<pk>/', views.show_channel, name='show_channel'),
    path('search/', views.search, name='search')

]
