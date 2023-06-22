from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . models import Profile, User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
