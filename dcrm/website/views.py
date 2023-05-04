from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def home(request):
    return render(request, 'index.html', {})


def login_user(request):
    if request.method == "POST":
        ...

    else:
        return render(request, 'login.html', {})


def register_user(request):
    if request.method == "POST":
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']

        url = reverse("home")

        return redirect(url, {"first_name": first_name, "last_name": last_name})

    else:
        return render(request, 'register.html', {})