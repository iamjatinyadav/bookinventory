from django.contrib import messages
from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def signup(request):
    return render(request, 'base/register.html')

def handlesignup(request):
    if request.method == 'POST':
        # get the post parameters
        fullname = request.POST['fname']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password1']

        if len(fullname) >20 :
            messages.error(request,"your username must be under 15 charactor.")
            return redirect('/')
        
        if password2 != password1:
            messages.error(request,"password and confirm password not same.")
            return redirect('register')

        myuser = User.objects.create_user(fullname, email, password1)
        myuser.save()
        messages.success(request,"your account has been successfully created")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')

def userlogin(request):
    return render(request, 'base/login.html')

def handlelogin(request):
    if request.method == 'POST':
        username = request.POST["fname"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invaild credentials, Please try again")
            return redirect('login')
    
    return HttpResponse('404 - Not Found') 


def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logout.")
    return redirect('home')


def allstore(request):
    return render(request, 'base/store.html')
