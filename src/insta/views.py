from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='login/')
def userdetail(request, *args, **kwargs):
    print(request)
    print(args)
    print(kwargs)
    return render(request, 'insta/dashboard.html', {})