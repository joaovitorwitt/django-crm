from django.shortcuts import render
from django.contrib.auth import autheticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'index.html', {})


def login_user(request):
    if request.method == "POST":
        ...

    else:
        return render(request, 'login.html', {})


def register_user(request):
    return render(request, 'register.html', {})