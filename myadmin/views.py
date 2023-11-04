from django.shortcuts import render,redirect
from myadmin.models import Country
# Create your views here.
def layout(request):
    context={}
    return render(request,'myadmin/common/layout.html')

def index(request):
    context={}
    return render(request,'myadmin/index.html')

def common_form(request):
    context={}
    return render(request,'myadmin/common_form.html',context)

def add_country(request):
    context={}
    return render(request,'myadmin/add_country.html',context)

def store_country(request):
    mycountry=request.POST['country']

    Country.objects.create(country=mycountry)
    return redirect('/myadmin/add_country')