from django.urls import path

# imports views file in the same directory
from . import views

app_name = 'website'

urlpatterns = [
    path("", views.home, name="home"),

]