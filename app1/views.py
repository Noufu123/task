from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from .models import *
# Create your views here.

def home(request):
    return render(request,'home.html')

def sign_up(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def signup_page(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        uname=request.POST['username']
        address=request.POST['address']
        mail=request.POST['email']
        num=request.POST['number']
        password=request.POST['password']
        confmpassword=request.POST['confirmpassword']

        #photo

        photo=request.FILES.get('photo')

        if password==confmpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'This User Name Is Already Exist')
                return render('sign_up')
            
            elif User.objects.filter(email=mail).exists():
                messages.info(request,'This Email Is Alreay Exist')
                return redirect('sign_up')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=mail,password=password)
                user.save()
                messages.success(request,'Successfully Registred')
                print("success")

                data=User.objects.get(id=user.id)
                user_data=usermodel(user_address=address,user_number=num,user_Photo=photo,user=data)
                user_data.save()
                messages.success(request,'successfully ragistred')
                print("successed")
                return redirect('login')

        else:
            #message info
            print("Password Is Not Matching")
            return redirect('sign_up')
        return redirect('load_user_login')
    else:
        return render(request,'signup.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password) #variavlename and html name

        user.save()
        return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('home')
