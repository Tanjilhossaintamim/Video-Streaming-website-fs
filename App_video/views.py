from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from App_login.models import Profile
from App_activity.models import Views, Comment, Subscribe, Like
from App_activity.forms import CommentForm
from .models import *
from .forms import ChannelCreateForm, VideoUploadForm

# Create your views here.


class AllVideos(ListView):
    model = Video
    template_name = 'App_video/all_videos.html'
    context_object_name = 'videos'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(public_view=True)


def video_details(request, pk):
    video = Video.objects.get(pk=pk)
    all_videos = Video.objects.filter(public_view=True)
    total_comment = Comment.objects.filter(video=video).count()
    video_comment_list = Comment.objects.filter(video=video)

    if request.user.is_authenticated:
        already_liked = Like.objects.filter(user=request.user, video=video)
        already_subscribe = Subscribe.objects.filter(
            subsciber=request.user, channel=video.channel.pk)
    else:
        already_subscribe = False
        already_liked = False
    if request.user.is_authenticated:
        Views.objects.get_or_create(viewer=request.user, video=video)

    ######## comment form ######
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                comment = form.save(commit=False)
                comment.user = request.user
                comment.video = video
                comment.save()
                return HttpResponseRedirect(reverse('App_video:video_details', kwargs={'pk': video.pk}))
            else:
                messages.warning(request, 'You are not Logged in !')
                return HttpResponseRedirect(reverse('App_login:login'))

    return render(request, 'App_video/video_details.html', context={'video': video, 'all_videos': all_videos, 'form': form, 'total_comment': total_comment, 'video_comment_list': video_comment_list, 'already_subscribe': already_subscribe, 'already_liked': already_liked})


@login_required
def create_channel(request):
    title = 'Create Your Channel'
    btn_name = 'Create'

    user_channel = Channel.objects.filter(user=request.user)
    if user_channel:
        messages.warning(request, 'You Have Already a channel !')
        return HttpResponseRedirect(reverse('App_login:profile'))
    else:
        user_profile = Profile.objects.get(user=request.user)
        if user_profile.is_fully_filled():
            form = ChannelCreateForm()
            if request.method == 'POST':
                form = ChannelCreateForm(request.POST, request.FILES)
                if form.is_valid():
                    channel = form.save(commit=False)
                    channel.user = request.user
                    channel.save()
                    messages.success(
                        request, 'You Create A Channel Successfully !')
                    return HttpResponseRedirect(reverse('App_login:channel'))
        else:
            messages.warning(request, 'Please Filled Profile Information !')

            return HttpResponseRedirect(reverse('App_login:edit_profile'))
    return render(request, 'App_video/create_channel.html', context={'form': form, 'title': title, 'btn_name': btn_name})


@login_required
def edit_channel(request):
    title = 'Edit Your Channel'
    btn_name = 'Save'

    user_channel = Channel.objects.get(user=request.user)

    form = ChannelCreateForm(instance=user_channel)
    if request.method == 'POST':
        form = ChannelCreateForm(
            request.POST, request.FILES, instance=user_channel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved Successfully !')
            form = ChannelCreateForm(instance=user_channel)

    return render(request, 'App_video/create_channel.html', context={'form': form, 'title': title, 'btn_name': btn_name})


@login_required
def channel_view(request):

    user_channel = Channel.objects.get(user=request.user)
    user_videos = Video.objects.filter(user=request.user, channel=user_channel)
    view = 0
    for video in user_videos:
        view += video.video_view.count()

    return render(request, 'App_video/channel.html', context={'user_videos': user_videos, 'view': view})


@login_required
def upload_video(request):
    title = 'Upload Your Video'
    btn_name = 'Upload'
    user_channel = Channel.objects.get(user=request.user)
    form = VideoUploadForm()
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.channel = user_channel
            video.save()
            messages.success(request, 'Video Uploaded Successfully !')
            return HttpResponseRedirect(reverse('App_video:channel'))
    return render(request, 'App_video/upload_video.html', context={'form': form, 'title': title, 'btn_name': btn_name})


@login_required
def edit_video(request, pk):
    title = 'Edit Your Video'
    btn_name = 'Save'
    video_info = Video.objects.get(pk=pk)
    form = VideoUploadForm(instance=video_info)
    if request.method == 'POST':
        form = VideoUploadForm(
            request.POST, request.FILES, instance=video_info)
        if form.is_valid():
            form.save()
            form = VideoUploadForm(instance=video_info)
            messages.success(request, 'Saved Successfull !')
            return HttpResponseRedirect(reverse('App_video:channel'))

    return render(request, 'App_video/upload_video.html', context={'form': form, 'title': title, 'btn_name': btn_name})


@login_required
def delete_video(request, pk):
    video = Video.objects.get(pk=pk)
    video.delete()
    messages.success(request, f'{video} Deleted Successfully !')
    return HttpResponseRedirect(reverse('App_video:channel'))


@login_required
def make_privet_video(request, pk):
    video = Video.objects.get(pk=pk)
    if video.public_view == True:
        video.public_view = False
        video.save()
        messages.info(request, 'Video Now Private !')
        return HttpResponseRedirect(reverse('App_video:channel'))
    else:
        messages.warning(request, 'Your Video Already Private !')
        return HttpResponseRedirect(reverse('App_video:channel'))


@login_required
def make_video_public(request, pk):
    video = Video.objects.get(pk=pk)
    if video.public_view == False:
        video.public_view = True
        video.save()
        messages.info(request, 'Video Now Public !')
        return HttpResponseRedirect(reverse('App_video:channel'))
    else:
        messages.warning(request, 'Your Video Already Public !')
        return HttpResponseRedirect(reverse('App_video:channel'))


def show_channel(request, pk):
    channel = Channel.objects.get(pk=pk)
    if request.user.is_authenticated:
        already_subscribe = Subscribe.objects.filter(
            subsciber=request.user, channel=channel.pk)
    else:
        already_subscribe = False

    channel_videos = Video.objects.filter(channel=channel)
    view = 0
    for video in channel_videos:
        view += video.video_view.count()

    return render(request, 'App_video/show_channel.html', context={'channel_videos': channel_videos, 'view': view, 'channel': channel, 'already_subscribe': already_subscribe})


def search(request):
    if request.method == 'POST':
        data = request.POST.get('search')
        videos = Video.objects.filter(title__startswith=data, public_view=True)
        if videos:
            video = True
        else:
            video = False

    return render(request, 'App_video/search.html', context={'videos': videos, 'video': video})
