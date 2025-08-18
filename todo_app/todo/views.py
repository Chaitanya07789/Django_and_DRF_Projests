from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import Todo
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.method=='POST':
        fnm = request.POST.get("fnm")
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        print(fnm,email,pwd)
        my_user = User.objects.create_user(fnm,email,pwd)
        my_user.save()
        return render(request,'login.html')
    return render(request,"signup.html")

def loginn(request):
    if request.method=="POST":
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        print(fnm,pwd)
        my_user= authenticate(request, username=fnm,password=pwd)
        if my_user is not None:
            login(request,my_user)
            return redirect('/todo')
        else:
            return redirect('/login')

    return render(request,'login.html')

@login_required(login_url='/login')
def todo(request):
    if request.method=="POST":
        title = request.POST.get('title')
        print(title)
        obj = models.Todo(title=title,user=request.user)
        obj.save()
        res = models.Todo.objects.filter(user=request.user).order_by('-date')
        return redirect('/todo',{'res':res})
    
    res = models.Todo.objects.filter(user=request.user).order_by('-date')
    return render(request,'todo.html',{'res':res})

@login_required(login_url='/login')
def edit_todo(request,id):
    if request.method=="POST":
        title = request.POST.get('title')
        print(title)
        obj = models.Todo.objects.get(id=id)
        obj.title = title
        obj.save()
        return redirect('/todo')
    
    obj = models.Todo.objects.get(id=id)
    return render(request,'edit_todo.html',{'obj':obj})

@login_required(login_url='/login')
def delete_todo(request,id):
    obj = models.Todo.objects.get(id=id)
    obj.delete()
    return redirect('/todo')

def signout(request):
    logout(request)
    return redirect('/login')