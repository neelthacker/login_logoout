from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SignUpForm()
    return render(request,'account/signup.html',{'form':fm})

def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password = upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
                    
        return render(request,'account/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'account/profile.html',{'name': request.user})
    else:
        return HttpResponseRedirect('/login/')

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')
