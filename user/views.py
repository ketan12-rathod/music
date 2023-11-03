from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from user.models import UserRegister
# Create your views here.
def layout(request):
    context={}
    return render(request,'user/common/layout.html',context)

def index(request):
    context={}
    return render(request,'user/index.html',context)

def register(request):
    context={}
    return render(request,'user/register.html',context)

def register_store(request):
    myaddress=request.POST['addr']
    myfirst_name=request.POST['fname']
    mylast_name=request.POST['lname']
    myemail=request.POST['email']
    myusername=request.POST['uname']
    mypassword=request.POST['password']
    mycpassword=request.POST['cpassword']

    if mycpassword == mypassword :
        user=User.objects.create_user(first_name=myfirst_name,last_name=mylast_name,email=myemail,username=myusername)
        UserRegister.objects.create(address=myaddress,user_id=user.id)
        return redirect('/user/index')
    else:
        return redirect('/user/register')