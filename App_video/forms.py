from django.forms import ModelForm
from .models import Channel, Video


class ChannelCreateForm(ModelForm):
    class Meta:
        model = Channel
        fields = ['channel_name', 'channel_logo', 'channel_desc']


class VideoUploadForm(ModelForm):
    class Meta:
        model = Video
        exclude = ['user', 'channel']
