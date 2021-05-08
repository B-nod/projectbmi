from django.urls import path
from useraccount.views import UserLogin, signup_view

app_name = "user"

urlpatterns = [
    path('login/', UserLogin.as_view(), name="login"),
    path('register/', signup_view, name="register"),
]