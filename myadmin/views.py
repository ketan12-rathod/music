from django.shortcuts import render,redirect
from myadmin.models import Country,State
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

def common_table(request):
    context={}
    return render(request,'myadmin/common_table.html',context)

def all_country(request):
    result=Country.objects.all()
    context={'result':result}
    return render(request,'myadmin/all_country.html',context)

def delete_country(request,id):
    result=Country.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_country')

def add_state(request):
    country=Country.objects.all()
    context={'country':country}
    return render(request,'myadmin/add_state.html',context)

def store_state(request):
    mystate=request.POST['state']
    mycountry=request.POST['country']
    
    State.objects.create(state=mystate,country_id=mycountry)
    return redirect('/myadmin/add_state')
