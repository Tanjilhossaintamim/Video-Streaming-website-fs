from django.db import models
from django.conf import settings


# Create your models here.
class Channel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_channel')
    channel_logo = models.ImageField(upload_to='channel_logo')
    channel_name = models.CharField(max_length=20)
    channel_desc = models.TextField(verbose_name='Channel Description')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.channel_name


class Video(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='user_video')
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name='channel_video')
    video = models.FileField(upload_to='channel_videos')
    thumbnail = models.ImageField(upload_to='thambnails')
    title = models.CharField(max_length=255)
    video_desc = models.TextField(verbose_name='Video Description')
    public_view = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']
