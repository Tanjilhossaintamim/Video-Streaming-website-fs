from django.db import models
from django.conf import settings
from App_video.models import Video, Channel

# Create your models here.


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='user_like')
    video = models.ForeignKey(Video, on_delete=models.CASCADE,related_name='like_video')


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='user_comment')
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['-comment_date']


class Subscribe(models.Model):
    subsciber = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_subscribe')
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name='subscribed_channel')


class Views(models.Model):
    viewer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_view')
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, related_name='video_view')
    
    class Meta:
        verbose_name_plural='Views'
