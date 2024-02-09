from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from .forms import *
from .models import *


def register(requset):
    if requset.method == 'POST':
        form = UserRegisterForm(requset.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['user_name']
                                            , email=data['email']
                                            , first_name=data['first_name']
                                            , last_name=data['last_name']
                                            , password=data['password_2'])
            user.save()
            messages.success(requset, 'you register successful', 'warning')

            return redirect('home:home')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(requset, 'accounts/register.html', context)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['user'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you login successful', 'success')
                return redirect('home:home')
            else:
                messages.error(request, 'username or password is wrong', 'danger')
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)



def user_logout(request):
    logout(request)
    messages.success(request, 'you logout successful', 'success')
    return redirect('home:home')
@login_required(login_url='accounts:login')
def user_profile(request):
    profile = Profile.objects.get(user_id=request.user.id)
    return render(request, 'accounts/profile.html', {'profile': profile})
@login_required(login_url='accounts:login')
def user_update(requset):
    if requset.method == 'POST':
        user_form = UserUpdateForm(requset.POST, instance=requset.user)
        profile_form = ProfileUpdateForm(requset.POST, instance=requset.user.profile)
        if user_form and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(requset, 'Your edit was done successfully', 'success')
    else:
        user_form = UserUpdateForm(instance=requset.user)
        profile_form = ProfileUpdateForm(instance=requset.user.profile)

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(requset, 'accounts/UpdateProfile.html', context)
@login_required(login_url='accounts:login')
def change_password(requset):
    if requset.method == 'POST':
        form = PasswordChangeForm(requset.user, requset.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(requset, form.user)
            messages.success(requset, 'Your password has been successfully changed', 'success')
            return redirect('accounts:profile')
        else:
            messages.error(requset, 'Password is wrong', 'danger')
            return redirect('accounts:change')
    else:
        form = PasswordChangeForm(requset.user)

    return render(requset, 'accounts/ChangePassword.html', {'form': form})
