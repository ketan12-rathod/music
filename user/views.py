from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from company.models import Add_Song
from myadmin.models import Country
from user.models import UserRegister
from django.contrib import messages,auth
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.
def layout(request):
    id=request.user.id
    result=UserRegister.objects.get(user_id=id)
    context={'result':result}
    return render(request,'user/common/layout.html',context)

def index(request):
    id=request.user.id
    song=Add_Song.objects.all()
    result=UserRegister.objects.get(user_id=id)
    context={'result':result,'song':song}
    return render(request,'user/index.html',context)

def info(request):
    context={}
    return render(request,'user/user_info.html',context)

def register_store(request):
    myfirst_name=request.POST['fname']
    myemail=request.POST['email']
    myusername=request.POST['uname']
    mypassword=request.POST['password']
    mypic=request.FILES['pic']

    mylocation= os.path.join(settings.MEDIA_ROOT, 'upload')
    obj=FileSystemStorage(location=mylocation)
    obj.save(mypic.name,mypic)
   
    user=User.objects.create_user(first_name=myfirst_name,email=myemail,username=myusername,password=mypassword)
    UserRegister.objects.create(profile_pic=mypic.name,user_id=user.id)
    return redirect('/user/login')
    

def register(request):
    context={}
    return render(request,'user/register.html',context)

def login(request):
    context={}
    return render(request,'user/user_login.html',context)

def login_check(request):
    myuname=request.POST['uname']
    mypassword=request.POST['password']

    result=auth.authenticate(request,username=myuname,password=mypassword)
    if result is not None:
        auth.login(request,result)
        return redirect('/user/add_profile')
    else:
        messages.info(request,'Please enter valid username or password!!')
        return redirect('/user/login')
    
def logout(request):
    auth.logout(request)
    return redirect('/user/login')

def add_profile(request):
    id=request.user.id
    country=Country.objects.all()
    result=UserRegister.objects.get(user_id=id)
    context={'result':result,'country':country}
    return render(request,'user/add_user_profile.html',context)