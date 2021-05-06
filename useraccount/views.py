from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def login(request):
    form = AuthenticationForm(request.POST or None)
    context = {"form":form}
    return render(request, "login.html", context)
