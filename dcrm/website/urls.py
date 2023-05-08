# imports views file in the same directory
from . import views
from django.urls import path

app_name = 'website'

urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout")
]