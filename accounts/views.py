from django.shortcuts import render,reverse,redirect
from django.contrib.auth import authenticate,login, logout 
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect


def login_page(request):

    if request.method=="POST":
        email = request.POST.get('email')
        password=request.POST.get('password')

        if not User.objects.filter(email=email).exists():
            print('Email Does not exists')
        
        user=authenticate(username=email, password=password)
        print(user, "user ")
        if user:
            login(request,user)
            return redirect('/')
        else:
            print('Passswrod Incorect ')


    return render(request,'accounts/login.html')

def register_page(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=User.objects.filter(email=email)
        if user.exists():
            messages.add_message(request, messages.WARNING, "Email Already Exists.")
            return HttpResponseRedirect(request.path_info)


        user=User.objects.create(username=email, email=email)
        user.set_password(password)
        user.save()
        messages.add_message(request, messages.SUCCESS, "Registered Successfully.")

    return render(request,'accounts/register.html')

def logout_page(request):
    logout(request)
    return redirect('/')
