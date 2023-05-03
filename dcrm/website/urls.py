from django.urls import path

# imports views file in the same directory
from . import views

app_name = 'website'

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register")
]