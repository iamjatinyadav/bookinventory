from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('Register', views.signup, name="Register"),
    path('login', views.userlogin, name="userlogin"),
    path('handlesignup', views.handlesignup, name="handlesignup"),
    path('handlelogin', views.handlelogin, name="handlelogin"),
    path('logout', views.handlelogout, name='handlelogout'),
    path('Stores', views.allstore, name='Stores'),


]