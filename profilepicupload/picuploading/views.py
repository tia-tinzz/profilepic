from django.shortcuts import render,HttpResponse,redirect
from .models import Product,Product1,Profilepic
from.form import ProductForm,UploadForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='loginform/')
def index(request):
    data=Product1.objects.all()
    img=Profilepic.objects.get(user=request.user)
    return render(request,"index.html",{'img':img,'obj':data})
def editform(request):
    if request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        expirydate=request.POST.get('expirydate')
        obj=Product()
        obj.name=name
        obj.price=price
        obj.save()
        exp=Product1()
        exp.expirydate=expirydate
        exp.product=obj
        exp.save()
        return redirect(index)
    else:
        return render(request,"producteditform.html")
def updatedata(request,id):
    myform=Product.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get('name')
        price=request.POST.get('price')
        expirydate=request.POST.get('expirydate')
        myform.name=name
        myform.price=price
        myform.expirydate=expirydate
        myform.save()
        return redirect(index)
    else:
        return render(request,"producteditform.html",{'form':myform})
def deletedata(request,id):
    data=Product.objects.get(id=id)
    data.delete()
    return redirect(index)
def registration(request):
    myform=UserCreationForm()
    if request.method=="POST":
        myform=UserCreationForm(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect(index)
        else:
            return render(request,"regform.html",{'form':myform})
    return render(request,"regform.html",{'form':myform})
def loginfn(request):
    myform=AuthenticationForm()
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            if username=='root':
                request.session['user']='admin'
                return redirect(adminpage)
            else:
                return render(request,"welcomeuser.html")
        else:
            return render(request,"regform.html",{'form':myform})
    return render(request,"login.html",{'form':myform})
def logoutfn(request):
    logout(request)
    return redirect(loginfn)
def adminpage(request):
    return render(request,"adminpage.html")
def welcomeuser(request):
    return render(request,"welcomeuser.html")
    
def uploadphoto(request):
    myform=UploadForm()
    if request.method=="POST":
        myform=UploadForm(request.POST,request.FILES)
        if myform.is_valid():
            myform.save()
            return redirect(index)
        else:
            return render(request,"upload.html",{'form':myform})
    return render(request,"upload.html",{'form':myform})
def addproduct(request):
    if request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        expirydate=request.POST.get('expirydate')
        obj=Product()
        obj.name=name
        obj.price=price
        obj.save()
        exp=Product1()
        exp.expirydate=expirydate
        exp.product=obj
        exp.save()
        return redirect(index)
    else:
        return render(request,"addproduct.html")
    
