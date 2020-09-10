from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import Permission


# Create your views here.

def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            perms=Permission.objects.get(id=35)

            newUser=User(username=username)
            newUser.set_password(password)
            
            newUser.save()

            #newUser.user_permissions.add(perms)
            

            return redirect("index")

        messages.warning(request,"şifreler işleşmiyor")
        form=RegisterForm()
        context={
            "form":form
        }

        return render(request,"register.html",context)
            




    else:

        form=RegisterForm()
        context={
            "form":form
        }

        return render(request,"register.html",context)
def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user is None:
            messages.warning(request,"Kullanıcı /parola hatalı")
            return render(request,"login.html",context)
        
        messages.success(request,"Giriş başarılı")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)
def logoutUser(request):
    messages.success(request,"Çıkış Yapıldı")
    logout(request)
    return redirect("index")
    