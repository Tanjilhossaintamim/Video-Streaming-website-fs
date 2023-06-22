from django.urls import path
from . import views
app_name = 'App_activity'

urlpatterns = [
    path('subscribe/<channel_id>/<video_id>/',
         views.subscribe, name='subscribe'),
    path('unsubscribe/<channel_id>/<video_id>/',
         views.unsubscribe, name='unsubscribe'),
    path('subscribe_user/<pk>/', views.subscribe_user, name='subscribe_user'),
    path('unsubscribe_user/<pk>/', views.unsubscribe_user, name='unsubscribe_user'),
    path('like/<pk>/', views.like, name='like'),
    path('unlike/<pk>/', views.unlike, name='unlike'),
]
