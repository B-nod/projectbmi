from django.urls import path
from useraccount.views import UserLogin, signup_view, logout_request, UserLogin, signup_view, user_profile, profile_edit, profile_create , my_profile

app_name = "user"

urlpatterns = [
    path('login/', UserLogin.as_view(), name="login"),
    path('register/', signup_view, name="register"),
    path("profile/", user_profile, name="profile"),
    path("edit/<int:id>/",profile_edit, name="profile_edit"),
    path("create/", profile_create, name="profile_create"),
    path('logout/', logout_request, name="logout"),
    path("myprofile/",my_profile, name="my_profile"),
]