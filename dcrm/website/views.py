from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


# login page
def login_user(request):
    if request.method == "POST":
        # get the info the user typed
        username = request.POST['username']
        password = request.POST['password']

        # authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged in")
            return redirect('website:home')
        else:
            messages.error(request, "Something went wrong, Try again")
            return redirect("website:login")
        
    # if the method is GET
    else:
        return render(request, 'login.html', {})




def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect("website:login")



# register page
def register_user(request):
    if request.method == "POST":
        ...

    else:
        return render(request, 'register.html', {})
    