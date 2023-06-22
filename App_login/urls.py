from django.urls import path
from . import views

app_name = 'App_login'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password')

]
