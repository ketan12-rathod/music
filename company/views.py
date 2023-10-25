from django.shortcuts import render,redirect
from company.models import Contact,Register,Add_Song,Add_Video
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.
def layout(request):
    context={}
    return render(request,'company/common/layout.html',context)

def index(request):
    id=request.user.id
    result=Register.objects.get(user_id=id)
    context={'result':result}
    return render(request,'company/index.html',context)

def contact(request):
    context={}
    return render(request,'company/contact.html',context)

def store_contact(request):
    mymessage=request.POST['message']
    myname=request.POST['name']
    myemail=request.POST['email']
    mysubject=request.POST['subject']
    user=request.user.id

    Contact.objects.create(message=mymessage,subject=mysubject,name=myname,email=myemail,user_id=user)
    return redirect('/company/contact')

def common_form(request):
    context={}
    return render(request,'company/common_form.html',context)

def register(request):
    context={}
    return render(request,'company/register.html',context)

def store_register(request):
    myname=request.POST['first_name']
    mylast_name=request.POST['last_name']
    myEMAIL=request.POST['EMAIL']
    mycity=request.POST['city']
    mycountry=request.POST['country']
    myuser_name=request.POST['user_name']
    mypassword=request.POST['password']
    mycpassword=request.POST['cpassword']
    myphoto=request.FILES['photo']

    mylocation=os.path.join(settings.MEDIA_ROOT, 'upload')
    obj=FileSystemStorage(location=mylocation)
    obj.save(myphoto.name,myphoto)

    if mycpassword == mypassword:
        user=User.objects.create_user(first_name=myname,last_name=mylast_name,email=myEMAIL,username=myuser_name,password=mypassword)
        Register.objects.create(city=mycity,country=mycountry,user_id=user.id)
        messages.info(request,"Register Successfully...")
        return redirect('/company/login')
    
    else:
        messages.info(request,"Password Is Not Matching!..")
        return redirect('/company/register')

def login(request):
    context={}
    return render(request,'company/login.html',context)

def login_check(request):
    myuser_name=request.POST['user_name']
    mypassword=request.POST['password']
    
    result=auth.authenticate(request,username=myuser_name,password=mypassword)

    if result is not None:
        auth.login(request,result)
        return redirect('/company/index')
    else:
        messages.info(request,'Please Enter Valid Username Or Password!..')
        return redirect('/company/register')
    
def add_song(request):
    context={}
    return render(request,'company/add_song.html',context)

def store_song(request):
    song = request.POST['song']
    singer_name = request.POST['singer_name']
    musician = request.POST['musician']
    mp3File = request.FILES['mp3File']
    imgFile = request.FILES['img']  # Assuming you have an input field named 'imgFile' for the image file

    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    
    obj = FileSystemStorage(location=mylocation)
    obj.save(mp3File.name, mp3File)  # Save MP3 file
    obj.save(imgFile.name, imgFile)  # Save image file

    Add_Song.objects.create(s_title=song, s_name=singer_name, m_name=musician, mp3=mp3File.name, img=imgFile.name, user_id=request.user.id)
    return redirect('/company/add_song')

def all_song(request):
    id=request.user.id
    result=Add_Song.objects.filter(user_id=id)
    context={'result':result}
    return render(request,'company/all_song.html',context)

def logout(request):
    auth.logout(request)
    return redirect('/company/login')

def delete_song(request,id):
    result=Add_Song.objects.get(pk=id)
    result.delete()
    return redirect('/company/all_song')

def add_video(request):
    context={}
    return render(request,'company/add_video.html',context)

def store_video(request):
    song = request.POST['song']
    singer_name = request.POST['singer_name']
    musician = request.POST['musician']
    mp4File = request.FILES['mp4File']
    imgFile = request.FILES['img']  # Assuming you have an input field named 'imgFile' for the image file

    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    
    obj = FileSystemStorage(location=mylocation)
    obj.save(mp4File.name, mp4File)  # Save MP3 file
    obj.save(imgFile.name, imgFile)  # Save image file

    Add_Video.objects.create(s_title=song, s_name=singer_name, m_name=musician, mp4=mp4File.name, img=imgFile.name, user_id=request.user.id)
    return redirect('/company/add_song')

def all_video(request):
    id=request.user.id
    result=Add_Video.objects.filter(user_id=id)
    context={'result':result}
    return render(request,'company/all_video.html',context)

def delete_video(request,id):
    result=Add_Video.objects.get(pk=id)
    result.delete()
    return redirect('/company/all_video')