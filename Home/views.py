from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Customer,item
from .forms import addform, updateform, itemaddform, itemupdateform
# Create your views here.
def index(request):
    Item = item.objects.all()
    cont ={
        'item':Item
    }
    return render(request,'Home/index.html',cont)

def customer(request):
    Customers = Customer.objects.all()
    cont ={
        'Customers':Customers
    }
    return render(request,'Home/customer.html',cont)

def add_customer(request):
    form = addform()
    if request.method == 'POST':
        form = addform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customer')
    return render(request,'Home/add_customer.html',{'form':form})
    

def update_customer(request,id):
    Customers = Customer.objects.get(pk=id)
    form = updateform(instance = Customers)
    if request.method == 'POST':
        form = updateform(request.POST, request.FILES, instance=Customers)
        if form.is_valid():
            form.save()
            return redirect('customer')
    return render(request,'Home/update.html',{'form':form})

def delete_customer(request,id):
    Customers = Customer.objects.get(pk=id)
    Customers.delete()
    return redirect('customer')

def about(request):
    return render(request,'Home/about.html')




def check(request):
    Customers = Customer.objects.all()
    cont ={
        'Customers':Customers
    }
    return render(request,'Home/check.html',cont)


def add_item(request):
        form = itemaddform()
        if request.method == 'POST':
            form = itemaddform(request.POST,request.FILES)
            if form.is_valid():
                form.save()
            return redirect('index')
        return render(request,'Home/add_item.html',{'form':form})

def update_item(request,id):
    Item = item.objects.get(pk=id)
    form = itemupdateform(instance = Item)
    if request.method == 'POST':
        form = itemupdateform(request.POST, request.FILES, instance=Item)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'Home/update_item.html',{'form':form})


def delete_item(request,id):
    Item = item.objects.get(pk=id)
    Item.delete()
    return redirect('index')

def retrive_item(request,id):
    Item = item.objects.get(pk=id)
    con = {
        'item':Item
    }
    return render (request,'Home/retrive.html',con)

def user(request):
    Customers = Customer.objects.all()
    cont ={
        'Customers':Customers
    }
    return render(request,'Home/user.html',cont)