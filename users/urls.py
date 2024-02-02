from django.urls import path
from .views import UserRegisterView,CustomUserLogin, LogoutView,ProfileView,ProfileUpdateView

app_name='users'
urlpatterns=[
    path('register/',UserRegisterView.as_view(), name='regis'),
    path('login/', CustomUserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile_update/', ProfileUpdateView.as_view(), name='profile_update'),

]