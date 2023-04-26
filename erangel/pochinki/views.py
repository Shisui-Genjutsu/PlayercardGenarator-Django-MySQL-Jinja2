from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from pochinki.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def BlogPage(request):
        # if request.method == 'GET':
            q = request.GET.get('q') if request.GET.get('q')!=None else ''
            bfm = Blog.objects.all()
            bm = Blog.objects.filter(
                 Q(name__icontains = q)|
                 Q(gun__icontains = q)|
                 Q(type__icontains = q)|
                 Q(id__icontains = q)
                 ).order_by('username')
            gunlist=[]
            unique_guns = []
            for i in bfm:
                gunlist.append(i.gun)
            [unique_guns.append(j) for j in gunlist if j not in unique_guns]

            return render(request,'pochinki/index.html',{'bm':bm, 'ug':unique_guns})
        # else:
        #     bm = Blog.objects.all()
        #     return render(request,'pochinki/index.html',{'bm':bm})
def navabar_page(request):
    return render(request, 'pochinki/navbar.html', {})
##### CURD Operations #####
@login_required(login_url='login')
def add_player(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gun = request.POST.get('gun')
        type = request.POST.get('type')
        username = request.POST.get('username')
        player = Blog(name=name, gun=gun, type=type, username_id=username)
        player.save()
        return redirect('home')   
    return render(request, 'pochinki/index.html',{})

@login_required(login_url='login')
def edit_player(request, id):
    bum = Blog.objects.get(id=id)
    if request.method=='POST':
        if request.user != bum.username:
            return HttpResponse("you are not allowed to do this action. login to countinue")
        name = request.POST.get('ename')
        gun = request.POST.get('egun')
        type = request.POST.get('etype')
        username = request.POST.get('eusername')
        bem = Blog(
            id = id,
            name=name,
            gun=gun,
            type=type,
            username_id=username
                   )
        bem.save()
        return redirect('home')
    return render(request, 'pochinki/index.html',{'bum':bum.username})

@login_required(login_url='login')
def delete_player(request, id):
    bdm=Blog.objects.get(id = id)
    if request.user != bdm.username:
        return HttpResponse("you are not allowed to do this action. login to countinue")
    Blog.objects.filter(id = id).delete()
    return redirect('home')
##### CURD Operations #####
##### Login/Logout/Register #####
def login_user(request):
    page = 'login'
    #restrict user not to relogin
    if request.user.is_authenticated:
        return redirect('home')
    #restrict user not to relogin
    if request.method == 'POST':
        username = request.POST.get('lusername')
        password = request.POST.get('lpassword')
        try:
            user = Blog.objects.get(username=username)
        except:
            messages.error(request, "Uer not found")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Check Credential")
    return render(request, 'pochinki/login_register.html', {'page':page})

def logout_user(request):
    logout(request)
    return redirect("home")

def use_register(request):
    # form = UserCreationForm()
    form = CustomUserCreationForm()
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "error occured while registering")
    return render(request, 'pochinki/login_register.html', {'form':form})
##### Login/Logout/Register #####

##### Others #####
def akatsuki(request):
    return render(request, 'pochinki/form1.html', {})
##### Others #####