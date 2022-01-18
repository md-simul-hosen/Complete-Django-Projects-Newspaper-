from Tools.scripts.make_ctype import method
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import info
from .models import products
from django.contrib import messages


def home(request):
    alldata = products.objects.all()
    context = {'products': alldata}
    print(alldata)
    return render(request, 'index.html', context)


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['con_password']
        if password == con_password:
            if User.objects.filter(username=name).exists():
                messages.error(request, 'Username already exist!')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exist!')
            else:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.error(request, 'Password does not match !')
    else:
        pass
    return render(request, 'register.html')


def loginto(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Username or Password invalid!')
    return render(request, 'login.html')


def post(request):
    if request.method == 'POST':
        posts = products()
        posts.heading = request.POST.get('heading')
        posts.description = request.POST.get('details')
        posts.date = request.POST.get('date')
        if len(request.FILES) != 0:
            posts.img = request.FILES['img']

        posts.save()
    return render(request, 'post.html')


def profile(request):
    return render(request, 'profile.html')


def userlogout(request):
    logout(request)
    messages.success(request, 'Logout successfully!')
    return redirect('login')


def forgot(request):
    return render(request, 'forgot.html')
