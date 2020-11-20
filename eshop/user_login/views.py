from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import*
from .models import*


#user loging
def user_loging(request):
    loging_form = UserLogingForm()
    if request.method == 'POST':
        loging_form = UserLogingForm(request.POST)
        if loging_form.is_valid():    
            name = loging_form.cleaned_data['name']
            password = loging_form.cleaned_data['password']
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                error_loging = 'The email and password that you entered did not match our records. Please double-check and try again.'
                context = {
                    'loging_form':loging_form,
                    'error_loging':error_loging,
                }
                return render(request, 'login.html', context)
    context = {
        'loging_form':loging_form
    }
    return render(request, 'login.html', context)


#user logout
def user_logout(request):
    logout(request)
    return redirect('/')