from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    current_user = request.user
    username = current_user.username
    email = current_user.email

    return render(request, 'profile.html', {'username': username, 'email': email})


def login_view(request):
    return render(request, 'login.html')
