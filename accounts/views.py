from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout

p=""
def signup(request):
    if request.method == 'POST':
        p=request.POST['username']
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'این نام کاربری قبلا در سیستم ثبت شده است'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'پسورد مثل هم نمی باشد'})
    else:
        return render(request,'accounts/signup.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password,)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
    else:
        return render(request,'accounts/login.html',{'error':'نام کاربری یا رمز عبور اشتباه است'})

def logout(request):
    if request.method == 'POST':

        auth.logout(request)
        return render(request,'accounts/signup.html')
    else:
        return render(request,'accounts/signup.html',{'error':'خروج با مشکل روبرو شد'})
