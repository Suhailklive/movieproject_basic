from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib import messages
from django.shortcuts import redirect
from .models import Movie


def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('movieapp:home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, 'User created successfully')
        return redirect('movieapp:login_view')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('movieapp:home')



