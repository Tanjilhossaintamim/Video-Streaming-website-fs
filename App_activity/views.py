from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from App_video.models import Video, Channel
from .models import Comment, Subscribe, Like


# Create your views here.
@login_required
def subscribe(request, channel_id, video_id):
    channel = Channel.objects.get(pk=channel_id)
    Subscribe.objects.get_or_create(
        subsciber=request.user, channel=channel)

    return HttpResponseRedirect(reverse('App_video:video_details', kwargs={'pk': video_id}))


@login_required
def unsubscribe(request, channel_id, video_id):
    channel = Channel.objects.get(pk=channel_id)
    already_subscribe = Subscribe.objects.get(
        subsciber=request.user, channel=channel)
    if already_subscribe:
        already_subscribe.delete()
        return HttpResponseRedirect(reverse('App_video:video_details', kwargs={'pk': video_id}))


@login_required
def subscribe_user(request, pk):
    channel = Channel.objects.get(pk=pk)
    Subscribe.objects.get_or_create(
        subsciber=request.user, channel=channel)
    return HttpResponseRedirect(reverse('App_video:show_channel', kwargs={'pk': pk}))


@login_required
def unsubscribe_user(request, pk):
    channel = Channel.objects.get(pk=pk)
    already_subscribe = Subscribe.objects.get(
        subsciber=request.user, channel=channel)
    if already_subscribe:
        already_subscribe.delete()
    return HttpResponseRedirect(reverse('App_video:show_channel', kwargs={'pk': pk}))


@login_required
def like(request, pk):
    video = Video.objects.get(pk=pk)
    already_like = Like.objects.get_or_create(user=request.user, video=video)
    
    return HttpResponseRedirect(reverse('App_video:video_details', kwargs={'pk': video.pk}))


@login_required
def unlike(request, pk):
    video = Video.objects.get(pk=pk)
    already_like = Like.objects.filter(user=request.user, video=video)
    if already_like:
        already_like[0].delete()
    return HttpResponseRedirect(reverse('App_video:video_details', kwargs={'pk': video.pk}))
