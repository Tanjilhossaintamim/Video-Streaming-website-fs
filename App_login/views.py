from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileForm
from .models import Profile

# Create your views here.


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully !')

            return HttpResponseRedirect(reverse('App_login:login'))
    return render(request, 'App_login/signup.html', context={'form': form})


def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, 'Login Successfull !')
                return HttpResponseRedirect(reverse('App_video:home'))

    return render(request, 'App_login/login.html', context={'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.warning(request, 'You are Not Logged in !')
    return HttpResponseRedirect(reverse('App_login:login'))


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            form = ProfileForm(instance=profile)

            messages.success(
                request, 'Profile Information Saved Successfully !')
            return HttpResponseRedirect(reverse('App_login:profile'))

    return render(request, 'App_login/edit_profile.html', context={'form': form})


@login_required
def profile(request):
    current_user = Profile.objects.get(user=request.user)
    return render(request, 'App_login/profile.html', context={'current_user': current_user})


@login_required
def change_password(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Change Successfully !')
            return HttpResponseRedirect(reverse('App_login:profile'))
    return render(request, 'App_login/change_password.html', context={'form': form})
