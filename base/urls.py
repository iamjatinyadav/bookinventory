from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('register', views.signup, name="register"),
    path('login', views.login, name="login"),
    path('handlesignup', views.handlesignup, name="handlesignup"),

]