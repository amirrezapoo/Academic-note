from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.base_user import AbstractBaseUser
from django.shortcuts import render, redirect

from account.forms import LoginForm, RegisterForm,EditUserForm
from account.models import User


# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['auth'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect("/")
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect("/")


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            return redirect('/')

    return render(request, 'account/register.html', {'form': form})


def profile(request):
    form = EditUserForm(instance=request.user)
    if request.method =="POST":
        form = EditUserForm(instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    return render(request, 'account/profile.html', {'form': form})

