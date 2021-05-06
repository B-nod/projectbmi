from django.urls import path
from useraccount.views import login

app_name = "user"

urlpatterns = [
    path('login/', login, name="login"),
]