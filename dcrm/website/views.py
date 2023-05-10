from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record



# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect("website:login")

    records = Record.objects.all()

    return render(request, 'index.html', {'records': records})


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



# logout function   
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect("website:login")



# register page
def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            # authenticate user and log user in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, "You have successfully registerd, welcome")
            return redirect("website:home")

    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})
    

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    
    else:
        messages.error(request, "You do not have access to this page")
        return redirect("website:login")


def delete_customer(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)

        delete_record.delete()
        messages.success(request, "Record deleted successfully")
        return redirect("website:home")
    
    else:
        messages.error(request, "You dont have access to this page")
        return redirect("website:login")
    

def add_record(request):
    form = AddRecordForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()

        return render(request, "add_record.html", {'form': form})